
# cl: instagrapi.Client
def url2Location(cl, permalink):
    print(f"info: fetch location from permalink: {permalink}")
    media_id = cl.media_pk_from_url(f"https://www.instagram.com/p/{permalink}/")
    media_info = cl.media_info_v1(media_id).dict()
    if "location" not in media_info:
        print(f"error: not found location in {media_info}")
        return None
    try:
        location = {
            "lat": media_info["location"]["lat"],
            "lng": media_info["location"]["lng"],
            "locationId": media_info["location"]["external_id"],
            "name": media_info["location"]["name"],
        }
    except Exception as e:
        print(f"info: {permalink} is no location tag:( ({e})")
        return None
    for _, value in location.items():
        if value == None or value == "":
            return None
    return location

