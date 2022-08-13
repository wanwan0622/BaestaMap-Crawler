import requests

# Get hashtag id from hashtag word
def get_hashtag_id(query, credentials):
    INSTAGRAM_ID = credentials["instagram_id"]
    ACCESS_TOKEN = credentials["access_token"]

    id_search_url = f"https://graph.facebook.com/ig_hashtag_search?user_id={INSTAGRAM_ID}&q={query}&access_token={ACCESS_TOKEN}"
    response = requests.get(id_search_url)
    hashtag_id = response.json()["data"][0]["id"]
    return hashtag_id # str

# add Hashtag Id on Firestore
def addHashTagId(fs, credentials):
    hashTags = fs.db.collection("hashTagNoId").stream()
    for hashTag in hashTags:
        query = hashTag.get('hashTag')
        if not hashTag.exists:
            continue
        hashtag_id = get_hashtag_id(query, credentials)
        doc_ref = fs.db.collection('hashTag').document()
        doc_ref.set(
            {
                "hashTag": query,
                "hashTagId": hashtag_id,
                "lastUpdate": None
            }
        )
        tag_no_id_ref = fs.db.collection('hashTagNoId').document(hashTag.id)
        tag_no_id_ref.delete()
