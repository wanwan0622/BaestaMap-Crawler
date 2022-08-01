from pip import main
import requests
import json
import requests

def get_post_id_from_tag(hashtag_id:str, serch_type:str, credentials:dict):
    INSTAGRAM_ID = credentials["instagram_id"]
    ACCESS_TOKEN = credentials["access_token"]

    fields = [
        "id",
        "permalink",
        "timestamp",
    ]
    fields_str = ",".join(fields)
    limit = 100
    url = f"https://graph.facebook.com/{hashtag_id}/{serch_type}?user_id={INSTAGRAM_ID}&access_token={ACCESS_TOKEN}&fields={fields_str}&limit={limit}"
    response = requests.get(url)
    json_data = response.json()

    posts = []
    for post_data in json_data["data"]:
        post = {
            "post_id": post_data["permalink"].rstrip("/").split("/")[-1],
            "timestamp": post_data["timestamp"],
        }
        posts.append(post)
    return posts

if __name__ == "__main__":
    with open("credencials.json") as f:
        credentials = json.load(f)

    hashtag_id = "17841562042082021" # 新宿ランチ
    serch_type = "top_media" # top_media or recent_media
    
    posts = get_post_id_from_tag(hashtag_id, serch_type, credentials)
    print(posts)
