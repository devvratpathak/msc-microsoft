from serpapi import GoogleSearch
import json
from geopy.geocoders import Nominatim


location = 'Vijayawada'


loc = Nominatim(user_agent="Geopy Library")
getLoc = loc.geocode(location)
print(getLoc.address)

long_lat ="@"+str(getLoc.latitude)+","+str(getLoc.longitude)+","+"14z"
print(long_lat)

params = {
  "api_key": "74667d45acf8d73e71f442fcea119219a9c88b09bb187292159a3fc88235289c",
  "engine": "google_maps",
  "type": "search",
  "google_domain": "google.com",
  "q": "Hospital",
  "ll": long_lat,
  "hl": "en" 
}

search = GoogleSearch(params)
results = search.get_dict()
local_result = results["local_results"]
for i in local_result:
    try:
        print(i['title'])
        print(i['photos_link'])
        print(i["phone"])
        print(i['website'])
    except:
        continue
