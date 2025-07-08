from lib.EnrichTool import EnrichTool
from lib.VirusTotal import VirusTotal

import requests as req
import re

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
    
    def getDomainReport(self, iocValue):
        domainIp = EnrichTool.dnsResolve(iocValue)
        report = self.getIpReport("IPv4", domainIp)
        report["iocType"] = "DOMAIN"
        report["iocValue"] = iocValue
        return report
    
    def getMailReport(self, iocValue):
        def getMailDomain(mail : str):
            for i in range(len(mail)):
                if mail[i] == "@":
                    return mail[i+1:]
            return ""
        
        domain = getMailDomain(iocValue)
        report = self.getDomainReport(domain)
        report["iocType"] = "MAILDOMAIN"
        report["iocValue"] = iocValue

        return report
    
    def getURLReport(self, iocValue):
        regex = r'https?://([a-zA-Z0-9.-]+)/?.*'
        matches = re.findall(regex, iocValue)
        if matches == []:
            return super().getURLReport(iocValue)
        domain = matches[0]
        report = self.getDomainReport(domain)
        report["iocType"] = "MAILDOMAIN"
        report["iocValue"] = iocValue

        return report