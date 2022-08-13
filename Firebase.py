from google.cloud import firestore

# cred = firestore.credentials.Certificate("./service_account.json")
# firestore.initialize_app(cred)

db = firestore.Client.from_service_account_json('./service-account.json')

hashTag_ref = db.collection("hashTag").document("rK0IClvvtfNkWK1JoUvY")
hashTag = hashTag_ref.get()
if not hashTag.exists:
    print("No such document!")
hashTag = hashTag.to_dict()
print(hashTag)