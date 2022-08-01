import requests
import json




def get_hash_id(query, credentials):
    INSTAGRAM_ID = credentials["instagram_id"]
    ACCESS_TOKEN = credentials["access_token"]
    
    id_search_url = f"https://graph.facebook.com/ig_hashtag_search?user_id={INSTAGRAM_ID}&q={query}&access_token={ACCESS_TOKEN}"
    response = requests.get(id_search_url)
    hash_id = response.json()["data"][0]["id"]
    return hash_id

if __name__ == "__main__":
    with open("credencials.json") as f:
        credentials = json.load(f)

    # 検索したいワード
    query = "新宿ランチ"
    hash_id = get_hash_id(query, credentials)
    print(hash_id)