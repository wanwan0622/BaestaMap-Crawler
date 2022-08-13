import json
import os

def getCredentials():
    if not os.path.exists("credentials.json"):
        print("credentials.json not found")
        exit()
    with open("credentials.json") as f:
        credentials = json.load(f)
        return credentials