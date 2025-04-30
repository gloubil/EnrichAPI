from lib.EnrichTool import EnrichTool

import requests as req

class AbuseIPDB(EnrichTool):

    BASE_URL = {
        "ip" : "https://api.abuseipdb.com/api/v2/check"
    }

    def __init__(self, apiKey):
        self.apiInfos = {"apiKey" : apiKey}

    def getReport(self, iocs):
        # Setup du rapport
        result = EnrichTool.BASE_REPORT.copy()
        result["EnrichToolName"] = "AbuseIPDB"
        result["ToolMessage"] = ""
        
        # Traitement des IOCs
        try:
            ip = iocs["ip"]
            url = f"{AbuseIPDB.BASE_URL["ip"]}?ipAddress={ip}&maxAgeInDays=30&verbose&key={self.apiInfos["apiKey"]}"
            response = req.get(url)
            value = response.json()["data"]["totalReports"]
            result["ToolMessage"] += f"totalReports : {value}\n"
        except:
            print(f"WARNING : ip report not handleled on {result["EnrichToolName"]}")

        return result
