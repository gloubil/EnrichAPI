from lib.EnrichTool import EnrichTool
from multiprocessing import Pool

def callTool(arg):
    tool, iocs = arg
    return tool.getReport(iocs)

class ReportGiver:
    """
        Classe Observer
        Stocke et appelle tous les EnrichTools enregistrés
    """

    def __init__(self):
        self.enrichTools = []

    def getReports(self, iocs : dict):
        with Pool(processes=len(self.enrichTools)) as p:
            args = [(tool, iocs) for tool in self.enrichTools]
            result = p.map(callTool, args)

            return result
    
    def register(self, tool : EnrichTool):
        self.enrichTools.append(tool)
        return len(self.enrichTools)

    def remove(self, tool : EnrichTool):
        def getIndex(l, e):
            for i in range(len(l)):
                if l[i] == e:
                    return i
            return -1
        toolIndex = getIndex(self.enrichTools, tool)

        if toolIndex != -1:
            return self.enrichTools.pop(toolIndex)
        print("WARNING : Tool not found in Tool list")
        return -1