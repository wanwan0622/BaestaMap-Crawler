from Firestore import FireStore
from instagrapi import Client
from credentials import getCredentials
from postLocation import post_location
from get_hashtag_id import addHashTagId
from get_posts import getPosts

print("info: initialize apps")
fs = FireStore()
credentials = getCredentials()

print("info: server start!")

mode = 2

if mode == 1:
    post_location(fs)
elif mode == 2:
    addHashTagId(fs, credentials)
elif mode == 3:
    cl = Client()
    cl.login(credentials["instagram_screen_name"], credentials["instagram_pw"])
    getPosts(fs, cl, credentials)
