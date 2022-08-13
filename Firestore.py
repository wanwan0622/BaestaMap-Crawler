from google.cloud import firestore

class FireStore:
    db = None
    def __init__(self):
        account_path = './service-account.json'
        self.db = firestore.Client.from_service_account_json(account_path)

