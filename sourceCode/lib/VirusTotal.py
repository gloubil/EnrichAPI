from lib.EnrichTool import EnrichTool

import requests as req
import re

class VirusTotal(EnrichTool):

    BASE_URL = {
        "url" : "https://www.virustotal.com/api/v3/urls/",
        "ip" : "https://www.virustotal.com/api/v3/ip_addresses/",
        "hash" : "https://www.virustotal.com/api/v3/files/",
        "mail" : "https://www.virustotal.com/api/v3/domains/"
    }

    def __init__(self, apikey):
        self.apiInfos = {
            "accept": "application/json",
            "x-apikey" : apikey
        }

    def getReport(self, iocs):
        # Setup du rapport
        result = EnrichTool.BASE_REPORT.copy()
        result["EnrichToolName"] = "VirusTotal"
        result["ToolMessage"] = ""
        
        # Traitement des IOCs
        try:
            ip = iocs["ip"]
            url = f"{VirusTotal.BASE_URL["ip"]}{ip}"
            response = req.get(url, headers=self.apiInfos)
            stats = response.json()["data"]["attributes"]["last_analysis_stats"]
            result["ToolMessage"] += f"score vt (ip) : {VirusTotal.getScore(stats)}\n"
        except KeyError:
            None
        except:
            print(f"WARNING : ip report not handleled on {result["EnrichToolName"]}")

        try:
            url_input = iocs["url"]
            url = f"{VirusTotal.BASE_URL["url"]}{url_input}"
            response = req.get(url, headers=self.apiInfos)
            stats = response.json()["data"]["attributes"]["last_analysis_stats"]
            result["ToolMessage"] += f"score vt (url) : {VirusTotal.getScore(stats)}\n"
        except KeyError:
            None
        except:
            print(f"WARNING : url report not handleled on {result["EnrichToolName"]}")

        try:
            hash = iocs["hash"]
            url = f"{VirusTotal.BASE_URL["hash"]}{hash}"
            response = req.get(url, headers=self.apiInfos)
            stats = response.json()["data"]["attributes"]["last_analysis_stats"]
            result["ToolMessage"] += f"score vt (hash) : {VirusTotal.getScore(stats)}\n"
        except KeyError:
            None
        except:
            print(f"WARNING : hash report not handleled on {result["EnrichToolName"]}")

        try:
            mail = iocs["mail"]
            domain = re.findall(r'@([^@]+)$', mail)[0]
            url = f"{VirusTotal.BASE_URL["mail"]}{domain}"
            response = req.get(url, headers=self.apiInfos)
            stats = response.json()["data"]["attributes"]["last_analysis_stats"]
            result["ToolMessage"] += f"score vt (mail) : {VirusTotal.getScore(stats)}\n"
        except KeyError:
            None
        except:
            print(f"WARNING : mail report not handleled on {result["EnrichToolName"]}")
        return result

    def getScore(stats):
        total = 0
        for arg in stats:
            total += int(stats[arg])
        score = f"{stats["malicious"]}/{total}"
        return score

