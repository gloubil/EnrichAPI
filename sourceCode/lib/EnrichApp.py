from lib.ReportGiver import ReportGiver

# Importez les classes dérivées de EnrichTool ici
from lib.AbuseIPDB import AbuseIPDB
from lib.HybridAnalysis import HybridAnalysis
from lib.VirusTotal import VirusTotal

class EnrichApp:
    """
        Classe main appelée par l'API
    """

    def __init__(self):
        self.reportGiver = ReportGiver()

        # Ajoutez les EnrichTools ici avec self.add(tool)
        self.add(AbuseIPDB("cc83387468b1c6082cdc512fac9e3d695b7564c4545bddaf2a18a12105da400a517e2234ea98614a"))
        self.add(HybridAnalysis("blckftyz10865d30smgbd0gf38633151vpndx8cn8b5802838n7lt9ne57b0f3c1"))
        self.add(VirusTotal("1484678fe361f05164d4bbc6e1042ff201463e2977682a68a2964d3b88df661d"))

    def add(self, tool):
        return self.reportGiver.register(tool)

    def delete(self, tool):
        return self.reportGiver.remove(tool)
    
    def run(self, iocs : dict):
        return self.reportGiver.getReports(iocs)