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

    def getReport(self, iocs):
        result = EnrichTool.BASE_REPORT.copy()
        result["EnrichToolName"] = "HybridAnalysis"
        result["ToolMessage"] = ""
        try:
            # Handle hash
            hash_ = iocs["hash"]
            url = HybridAnalysis.BASE_URL["hash"]
            response = req.post(url, headers=self.apiInfos, data={"hash" : hash_})
            value = response.json()[0]["verdict"]
            result["ToolMessage"] += f"verdict : {value}\n"
        except KeyError:
            None
        except:
            print(f"WARNING : hash report not handleled on {result["EnrichToolName"]}")
        return result
