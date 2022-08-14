from Firestore import FireStore
from instagrapi import Client
from credentials import getCredentials
from get_hashtag_id import addHashTagId
from tags_api import getPosts

print("info: initialize apps")
fs = FireStore()
credentials = getCredentials()
cl = Client()
cl.login(credentials["instagram_screen_name"], credentials["instagram_pw"])

print("info: server start!")

getPosts(fs, cl, credentials)