from Firestore import FireStore
from instagrapi import Client
from credentials import getCredentials
from post_location import post_location
from get_hashtag_id import addHashTagId
from get_posts import getPostsFromAPI, getPostsFromLibrary

print("info: initialize apps")
fs = FireStore()
credentials = getCredentials()

print("info: server start!")


mode = 5

if mode == 0:
    posts = fs.db.collection("posts").get()
    print(len(posts))
elif mode == 1:
    post_location(fs, "dataset/stations.txt")
elif mode == 2:
    addHashTagId(fs=fs, credentials=credentials)
elif mode == 3:
    cl = Client()
    cl.login(credentials["instagram_screen_name"], credentials["instagram_pw"])
    addHashTagId(fs=fs, cl=cl)
elif mode == 4:  # インスタが凍結されており、FBと紐づけられているので使いにくい
    cl = Client()
    cl.login(credentials["instagram_screen_name"], credentials["instagram_pw"])
    getPostsFromAPI(fs, cl, credentials)
elif mode == 5:
    cl = Client()
    cl.login(credentials["instagram_screen_name"], credentials["instagram_pw"])
    getPostsFromLibrary(fs, cl)
