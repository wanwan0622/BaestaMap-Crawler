def post_location(fs, filename):
    locations = []
    with open(filename, "r") as f:
        locations = f.read().split("\n")
    for idx, location in enumerate(locations):
        print(f"({idx+1}/{len(locations)}) Setting location: {location}")
        doc_ref = fs.db.collection("hashTagNoId").document()
        doc_ref.set({"hashTag": f"{location}ランチ"})
        doc_ref = fs.db.collection("hashTagNoId").document()
        doc_ref.set({"hashTag": f"{location}ディナー"})
        
        doc_ref = fs.db.collection("hashTagNoId").document()
        doc_ref.set({"hashTag": f"{location}駅ランチ"})
        doc_ref = fs.db.collection("hashTagNoId").document()
        doc_ref.set({"hashTag": f"{location}駅ディナー"})
