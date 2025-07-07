import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    AbuseIPDB_KEY=os.getenv('AbuseIPDB_KEY')
    HybridAnalisis_KEY=os.getenv('HybridAnalisis_KEY')
    VirusTotal_KEY=os.getenv('VirusTotal_KEY')
    OTX_KEY=os.getenv('OTX_KEY')