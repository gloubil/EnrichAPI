from lib.EnrichTool import EnrichTool

import requests as req

class AbuseIPDB(EnrichTool):

    BASE_URL = {
        "ip" : "https://api.abuseipdb.com/api/v2/check"
    }

    def __init__(self, apiKey):
        self.apiInfos = {"apiKey" : apiKey}
        self.toolName = "AbuseIPDB"


    def getIpReport(self, ipType, iocValue):

        url = f"{AbuseIPDB.BASE_URL['ip']}?ipAddress={iocValue}&maxAgeInDays=30&verbose&key={self.apiInfos['apiKey']}"
        response = req.get(url)
        value = response.json()['data']['totalReports']

        return {"iocType" : f"{ipType}", "iocValue" : iocValue, "report" : f"totalReports : {value}"}
    
    