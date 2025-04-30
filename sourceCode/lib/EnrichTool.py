class EnrichTool:
    """
        Interface EnrichTool Observable
    """
    BASE_REPORT = {"EnrichToolName" : "", "ToolMessage" : "field : value"}

    def getReport(self, iocs : dict):
        """
            Args :
                iocs -> dictionnaire avec les clés : ip, hash, mail, url

            Returns :
                Template de retour, Résultat de l'api utilisée
        """
        return EnrichTool.BASE_REPORT