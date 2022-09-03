from Firestore import FireStore
from instagrapi import Client
from credentials import getCredentials
from post_location import post_location
from get_hashtag_id import addHashTagId
from get_posts import getPosts, getPosts2

print("info: initialize apps")
fs = FireStore()
credentials = getCredentials()

print("info: server start!")

mode = 3

if mode == 1:
    post_location(fs, "dataset/stations.txt")
elif mode == 2:
    addHashTagId(fs=fs, credentials=credentials)
elif mode == 3:
    cl = Client()
    cl.login(credentials["instagram_screen_name"], credentials["instagram_pw"])
    addHashTagId(fs=fs, cl=cl)
elif mode == 4:
    cl = Client()
    cl.login(credentials["instagram_screen_name"], credentials["instagram_pw"])
    getPosts(fs, cl, credentials)
elif mode == 5:
    cl = Client()
    cl.login(credentials["instagram_screen_name"], credentials["instagram_pw"])
    getPosts2(fs, cl)
    