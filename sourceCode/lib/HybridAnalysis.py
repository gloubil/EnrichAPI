from lib.EnrichTool import EnrichTool

import requests as req

class HybridAnalysis(EnrichTool):

    BASE_URL = {
        "hash" : "https://hybrid-analysis.com/api/v2/search/hash"
    }

    def __init__(self, apiKey):
        self.apiInfos = {
            'api-key': apiKey,
            'User-Agent': 'Falcon Sandbox',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        self.toolName = "Hybrid Analysis"


    def getHashReport(self, hashType, iocValue):

        url = HybridAnalysis.BASE_URL['hash']
        response = req.post(url, headers=self.apiInfos, data={"hash" : iocValue})
        value = response.json()[0]['verdict']

        return {"iocType" : f"{hashType}", "iocValue" : iocValue, "report" : f"verdict : {value}"}