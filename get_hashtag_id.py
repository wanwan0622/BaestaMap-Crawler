import requests
import datetime

# Get hashtag id from hashtag word
def get_hashtag_id(query, credentials):
    INSTAGRAM_ID = credentials["instagram_id"]
    ACCESS_TOKEN = credentials["access_token"]

    id_search_url = f"https://graph.facebook.com/ig_hashtag_search?user_id={INSTAGRAM_ID}&q={query}&access_token={ACCESS_TOKEN}"
    response = requests.get(id_search_url)
    try:
        hashtag_id = response.json()["data"][0]["id"]
        return str(hashtag_id)
    except:
        return None

# add Hashtag Id on Firestore
def addHashTagId(fs, credentials):
    hashTags = fs.db.collection("hashTagNoId").stream()
    for idx, hashTag in enumerate(hashTags):
        print(
            f"({idx+1}) Setting hashtag: {hashTag.to_dict()}"
        )
        if not hashTag.exists:
            continue
        query = hashTag.get("hashTag")
        if query[0] == "－":
            continue
        hashtag_id = get_hashtag_id(query, credentials)
        if hashtag_id is not None:
            doc_ref = fs.db.collection("hashTag").document()
            doc_ref.set(
                {
                    "hashTag": query,
                    "hashTagId": hashtag_id,
                    "timestamp": datetime.datetime.now(tz=datetime.timezone.utc),
                }
            )
        tag_no_id_ref = fs.db.collection("hashTagNoId").document(hashTag.id)
        tag_no_id_ref.delete()
