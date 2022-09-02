def post_location(fs):
    locations = []
    with open("locations.txt", "r") as f:
        locations = f.read().split("\n")
    for idx, location in enumerate(locations):
        doc_ref = fs.db.collection("hashTagNoId").document()
        print(f"({idx+1}/{len(locations)}) Setting location: {location}")
        doc_ref.set({"hashTag": f"{location}ランチ"})
        # doc_ref.set({"hashTag": f"{location}ディナー"})
