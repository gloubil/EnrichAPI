from lib.EnrichTool import EnrichTool

import requests as req
import re
import base64

class VirusTotal(EnrichTool):

    BASE_URL = {
        "domain" : "https://www.virustotal.com/api/v3/domains/",
        "ip" : "https://www.virustotal.com/api/v3/ip_addresses/",
        "hash" : "https://www.virustotal.com/api/v3/files/",
        "mail" : "https://www.virustotal.com/api/v3/domains/",
        "url" : "https://www.virustotal.com/api/v3/urls/"
    }

    def __init__(self, apikey):
        self.apiInfos = {
            "accept": "application/json",
            "x-apikey" : apikey
        }
        self.toolName = "VirusTotal"

    def getScore(stats):
        total = 0
        for arg in stats:
            total += int(stats[arg])
        score = f"{stats['malicious']}/{total}"
        return score

    def getIpReport(self, ipType, iocValue):

        url = f"{VirusTotal.BASE_URL['ip']}{iocValue}"
        response = req.get(url, headers=self.apiInfos)
        stats = response.json()['data']['attributes']['last_analysis_stats']
        score = VirusTotal.getScore(stats)

        return {"iocType" : f"{ipType}", "iocValue" : iocValue, "report" : f"Score VT : {score}"}
    
    def getHashReport(self, hashType, iocValue):

        url = f"{VirusTotal.BASE_URL['hash']}{iocValue}"
        response = req.get(url, headers=self.apiInfos)
        stats = response.json()['data']['attributes']['last_analysis_stats']
        score = VirusTotal.getScore(stats)

        return {"iocType" : f"{hashType}", "iocValue" : iocValue, "report" : f"Score VT : {score}"}
    
    def getDomainReport(self, iocValue):

        url = f"{VirusTotal.BASE_URL['domain']}{iocValue}"
        response = req.get(url, headers=self.apiInfos)
        stats = response.json()['data']['attributes']['last_analysis_stats']
        score = VirusTotal.getScore(stats)

        return {"iocType" : "DOMAIN", "iocValue" : iocValue, "report" : f"Score VT : {score}"}
    
    def getMailReport(self, iocValue):

        def getMailDomain(mail : str):
            for i in range(len(mail)):
                if mail[i] == "@":
                    return mail[i+1:]
            return ""

        domain = getMailDomain(iocValue)
        
        if domain == "":
            return {"iocType" : "MAILDOMAIN", "report" : None}

        url = f"{VirusTotal.BASE_URL['mail']}{domain}"
        response = req.get(url, headers=self.apiInfos)
        stats = response.json()['data']['attributes']['last_analysis_stats']
        score = VirusTotal.getScore(stats)

        return {"iocType" : "MAILDOMAIN", "iocValue" : iocValue, "report" : f"Score VT : {score}"}
    
    def getURLReport(self, iocValue):
        url_id = base64.urlsafe_b64encode(iocValue.encode()).decode().strip("=")

        reponse = req.get(f"{VirusTotal.BASE_URL['url']}{url_id}", headers=self.apiInfos)

        stats = reponse.json()['data']['attributes']['last_analysis_stats']
        score = VirusTotal.getScore(stats)
        
        return {"iocType" : "URL", "iocValue" : iocValue, "report" : f"Score VT : {score}"}