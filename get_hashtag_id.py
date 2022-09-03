import requests
import datetime
import time

# Get hashtag id from hashtag word
def get_hashtag_id(query, credentials):
    INSTAGRAM_ID = credentials["instagram_id"]
    ACCESS_TOKEN = credentials["access_token"]

    id_search_url = f"https://graph.facebook.com/ig_hashtag_search?user_id={INSTAGRAM_ID}&q={query}&access_token={ACCESS_TOKEN}"
    response = requests.get(id_search_url)
    try:
        print(response.json())
        hashtag_id = response.json()["data"][0]["id"]
        return str(hashtag_id)
    except:
        return None


def get_hashtag_id2(query, cl):
    try:
        hashtag = cl.hashtag_info_gql(query)
        if "id" in hashtag.dict():
            return hashtag.dict()["id"]
        else:
            return False
    except Exception as e:
        print(e)
        if "'hashtag': None" in str(e):
            return False
        else:
            return None


# add Hashtag Id on Firestore
def addHashTagId(fs, credentials=None, cl=None):
    hashTags = fs.db.collection("hashTagNoId").stream()
    for idx, hashTag in enumerate(hashTags):
        print(f"({idx+1}) Setting hashtag: {hashTag.to_dict()}")
        if not hashTag.exists:
            continue
        query = hashTag.get("hashTag")
        if credentials is not None:
            hashtag_id = get_hashtag_id(query, credentials)
        elif cl is not None:
            hashtag_id = get_hashtag_id2(query, cl)
        print("hashtag_id:", hashtag_id)
        if hashtag_id is not None and hashtag_id is not False:
            doc_ref = fs.db.collection("hashTag").document()
            doc_ref.set(
                {
                    "hashTag": query,
                    "hashTagId": hashtag_id,
                    "timestamp": datetime.datetime.now(tz=datetime.timezone.utc),
                }
            )
        if hashtag_id is not None:
            print("removed!")
            tag_no_id_ref = fs.db.collection("hashTagNoId").document(hashTag.id)
            tag_no_id_ref.delete()
        time.sleep(3)
