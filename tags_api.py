import requests
import json

with open('credencials.json') as f:
    credentials = json.load(f)


INSTAGRAM_ID = credentials['instagram_id']
ACCESS_TOKEN = credentials['access_token']

# 検索したいワード
query = "新宿ランチ"

id_search_url = f"https://graph.facebook.com/ig_hashtag_search?user_id={INSTAGRAM_ID}&q={query}&access_token={ACCESS_TOKEN}"

response = requests.get(id_search_url)
hash_id = response.json()["data"][0]['id']
print(hash_id)

serch_type = "top_media"

url = (
    f"https://graph.facebook.com/{hash_id}/{serch_type}?user_id={INSTAGRAM_ID}&q={query}&access_token={ACCESS_TOKEN}&fields="
    + "id,media_type,media_url,permalink,like_count,comments_count,caption,timestamp,children{id,media_url}&limit=50"
)

response = requests.get(url)
json_data = response.json()
print(json_data)
