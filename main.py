from Firestore import FireStore
from get_hashtag_id import addHashTagId
from credentials import getCredentials

fs = FireStore()
credentials = getCredentials()

addHashTagId(fs, credentials)