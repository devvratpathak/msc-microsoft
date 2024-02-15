#Finds nearby hospitals/consultation institutes etc
from flask import Flask, request, jsonify
from serpapi import GoogleSearch
import json
from geopy.geocoders import Nominatim

app = Flask(__name__)

# Allow requests from http://127.0.0.1:5500
@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', 'http://127.0.0.1:5500')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Methods', 'POST')
    return response

@app.route('/submit_questions', methods=['POST'])
def submit_questions():
    data = request.get_json()
    questions = data.get('questions', {})

    # Process the questions as needed
    global location
    location =questions['question1']


    loc = Nominatim(user_agent="Geopy Library")
    getLoc = loc.geocode(location)
    print(getLoc.address)
    
    # printing latitude and longitude
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
    json_formatted_out = json.dumps(results, indent=2)
    print(json_formatted_out)



    return jsonify(status='success', message='Questions received successfully')


if __name__ == '__main__':
    app.run(debug=True)









