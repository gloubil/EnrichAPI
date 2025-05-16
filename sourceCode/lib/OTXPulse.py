try:
    from lib.EnrichTool import EnrichTool
except:
    from EnrichTool import EnrichTool

from OTXv2 import OTXv2
from OTXv2 import IndicatorTypes

from multiprocessing import Pool

class OTXPulse(EnrichTool):

    def __init__(self, apiKey, toShow = 3):
        self.apiKey = apiKey
        self.actToShow = toShow # Pules info to show

    def get_info(arg):
        otx, iocType, ioc = arg
        return otx.get_indicator_details_full(iocType, ioc)
    
    def getReport(self, iocs):
        # Setup du rapport
        result = EnrichTool.BASE_REPORT.copy()
        result['EnrichToolName'] = "OTX Pulse"
        result['ToolMessage'] = ""

        args = []

        otx = OTXv2(self.apiKey)

        try:
            ioc = iocs["ip"]
            if ioc != "" and ioc != None:
                args.append((otx, IndicatorTypes.IPv4, ioc))
        except KeyError:
            None
        except:
            print(f"WARNING : ip report not handleled on {result['EnrichToolName']}")

        try:
            ioc = iocs["url"]
            if ioc != "" and ioc != None:
                args.append((otx, IndicatorTypes.URL, ioc))
        except KeyError:
            None
        except:
            print(f"WARNING : url report not handleled on {result['EnrichToolName']}")

        try:
            ioc = iocs["hash"]
            if ioc != "" and ioc != None:
                args.append((otx, IndicatorTypes.FILE_HASH_SHA1, ioc))
        except KeyError:
            None
        except:
            print(f"WARNING : hash report not handleled on {result['EnrichToolName']}")

        try:
            ioc = iocs["mail"]
            if ioc != "" and ioc != None:
                args.append((otx, IndicatorTypes.EMAIL, ioc))
        except KeyError:
            None
        except:
            print(f"WARNING : mail report not handleled on {result['EnrichToolName']}")

        data = [OTXPulse.get_info(arg) for arg in args]

        # if __name__ == 'lib.OTXPulse': # AssertionError: daemonic processes are not allowed to have children
        #     with Pool(len(args)) as p:
        #         data = p.map(OTXPulse.get_info, args)


        for line in data:
            message = self.formatMessage(line)

            result['ToolMessage'] += message + "\n\n"

        return result



    def formatMessage(self, line):
        try:
            pulses = line['general']['pulse_info']['pulses']
            iocType = line['general']['type']
            iocValue = line['general']['indicator']

            message = ""

            toShow = self.actToShow

            if toShow > len(pulses):
                toShow = len(pulses)

            if len(pulses) != 0:
                for i in range(toShow):
                    pulse = pulses[i]
                    message += pulse['name'] + "\n"
            else: message = "No Activities"

            message = " | " + iocType + " : " + iocValue + " Activity :\n" + message

            return message
        except KeyError:
            return ""

