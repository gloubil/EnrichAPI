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
        self.otx = OTXv2(self.apiKey)
        self.toolName = "OTX Pulse"

        self.actToShow = toShow # Pulses info to show

    def get_info(self, iocType, iocValue):
        details = self.otx.get_indicator_details_full(indicator_type=iocType, indicator=iocValue)
        try:
            pulses = details['general']['pulse_info']['pulses']
        except KeyError:
            return None

        message = ""

        toShow = self.actToShow

        if toShow > len(pulses):
            toShow = len(pulses)

        if len(pulses) != 0:
            for i in range(toShow):
                pulse = pulses[i]
                message += pulse['name'] + " | "
            message = message[:-3]
        else: message = "No Activities Detected"

        return message
    
    def getIpReport(self, ipType, iocValue):

        if ipType == "IPv4":
            indicatorType = IndicatorTypes.IPv4
        elif ipType == "IPv6":
             indicatorType = IndicatorTypes.IPv6
        else:
            return {"iocType" : f"{ipType}", "iocValue" : "Not Handleled", "report" : None}
        
        infos = self.get_info(indicatorType, iocValue)

        if infos == None:
            return {"iocType" : f"{ipType}", "iocValue" : "Not Handleled", "report" : None}

        return {"iocType" : f"{ipType}", "iocValue" : iocValue, "report" : infos}
    
    def getHashReport(self, hashType, iocValue):

        if hashType == "SHA1":
            indicatorType = IndicatorTypes.FILE_HASH_SHA1
        elif hashType == "SHA256":
             indicatorType = IndicatorTypes.FILE_HASH_SHA256
        elif hashType == "MD5":
             indicatorType = IndicatorTypes.FILE_HASH_MD5
        else:
            return {"iocType" : f"{hashType}", "iocValue" : "Not Handleled", "report" : None}
        
        infos = self.get_info(indicatorType, iocValue)

        if infos == None:
            return {"iocType" : f"{hashType}", "iocValue" : "Not Handleled", "report" : None}

        return {"iocType" : f"{hashType}", "iocValue" : iocValue, "report" : infos}
    
    def getDomainReport(self, iocValue):
        
        infos = self.get_info(IndicatorTypes.DOMAIN, iocValue)

        if infos == None:
            return {"iocType" : "DOMAIN", "iocValue" : "Not Handleled", "report" : None}

        return {"iocType" : "DOMAIN", "iocValue" : iocValue, "report" : infos}
    
    def getMailReport(self, iocValue):

        infos = self.get_info(IndicatorTypes.EMAIL, iocValue)

        if infos == None:
            return {"iocType" : "MAIL", "iocValue" : "Not Handleled", "report" : None}

        return {"iocType" : "MAIL", "iocValue" : iocValue, "report" : infos}
