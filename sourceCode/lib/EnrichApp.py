from lib.ReportGiver import ReportGiver

# Importez les classes dérivées de EnrichTool ici
from lib.AbuseIPDB import AbuseIPDB
from lib.HybridAnalysis import HybridAnalysis
from lib.VirusTotal import VirusTotal
from lib.OTXPulse import OTXPulse

from Config import Config

class EnrichApp:
    """
        Classe main appelée par l'API
    """

    def __init__(self):
        self.reportGiver = ReportGiver()

        # Ajoutez les EnrichTools ici avec self.add(tool)
        self.add(AbuseIPDB(Config.AbuseIPDB_KEY))
        self.add(HybridAnalysis(Config.HybridAnalisis_KEY))
        self.add(VirusTotal(Config.VirusTotal_KEY))
        self.add(OTXPulse(Config.OTX_KEY))

    def add(self, tool):
        return self.reportGiver.register(tool)

    def delete(self, tool):
        return self.reportGiver.remove(tool)
    
    def run(self, iocs : dict):
        return self.reportGiver.getReports(iocs)
