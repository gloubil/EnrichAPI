class EnrichTool:
    """
        Interface EnrichTool Observable
    """
    
    def __init__(self):
        self.toolName = "ToolTemplate"



    def getReport(self, iocs : dict):
        """
            Args :
                iocs -> dictionnaire avec les clés : ip, hash, mail, url

            Returns :
                Rapport pour le Tool utilisé
        """
        output = {"EnrichToolName" : f"{self.toolName}", "reports" : []}
        reports = []

        def parseHash(iocValue):
            if iocValue == "":
                return "EmptyHASH"

            for i in range(len(iocValue)):
                if iocValue[i] == ":":
                    return iocValue[:i], iocValue[i+1:]
                
            return "SHA1", iocValue # Default hash algorithm

        for ioc in iocs:
            if iocs[ioc] != "" and iocs[ioc] != None:
                iocValue = iocs[ioc]
                try:
                    if ioc == "ip":
                        reports.append(self.getIpReport("IPv4", iocValue))

                    elif ioc == "hash":
                        hashType, hashValue = parseHash(iocValue)
                        reports.append(self.getHashReport(hashType, hashValue))

                    elif ioc == "domain":
                        reports.append(self.getDomainReport(iocValue))

                    elif ioc == "mail":
                        reports.append(self.getMailReport(iocValue))
                except Exception as e:
                    print(str(e))
        output["reports"] = reports

        return output


    
    def getIpReport(self, ipType, iocValue):
        return {"iocType" : f"{ipType}", "iocValue" : "Not Handleled", "report" : None}
    
    def getHashReport(self, hashType, iocValue):
        return {"iocType" : f"{hashType}", "iocValue" : "Not Handleled", "report" : None}
    
    def getDomainReport(self, iocValue):
        return {"iocType" : "DOMAIN", "iocValue" : "Not Handleled", "report" : None}
    
    def getMailReport(self, iocValue):
        return {"iocType" : "MAIL", "iocValue" : "Not Handleled", "report" : None}