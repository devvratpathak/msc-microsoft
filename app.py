from flask import Flask, render_template, request, redirect, url_for
from serpapi import GoogleSearch
from geopy.geocoders import Nominatim

app = Flask(__name__)

import openai

openai.api_key = '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'

def send_message(message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a chatbot."},
            {"role": "user", "content": message}
        ],
        max_tokens=100,
        temperature=0.7
    )
    return response['choices'][0]['message']['content']

@app.route('/mood', methods=['GET', 'POST'])
def mood():
    user_input = None
    bot_response = None

    if request.method == 'POST':
        user_input = request.form['user_input']
        mood_inp = "Interpret the person's mood using only one of the mood words listed, providing the closest interpretation possible. The words are Happy/Joyful, Sad, Angry, Fearful, Surprised, Disgusted, Excited, Content, Anxious, Depressed, Loving/Affectionate, Confused, Jealous, Guilty, Relieved. The sentence is: " + user_input
        bot_response = send_message(mood_inp)

    return render_template("mood.html", user_input=user_input, bot=bot_response)

@app.route("/vhelp", methods=['GET', 'POST'])
def vhelp():
    if request.method == 'POST':
        location = request.form.get('location')
        if location:
            loc = Nominatim(user_agent="Geopy Library")
            getLoc = loc.geocode(location)
            if getLoc:
                long_lat = "@" + str(getLoc.latitude) + "," + str(getLoc.longitude) + "," + "14z"
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
                local_results = results.get("local_results", [])
                hospitals = []
                for i in local_results:
                    try:
                        hospitals.append({
                            "title": i['title'],
                            "photos_link": i['photos_link'],
                            "phone": i["phone"],
                            "website": i['website'],
                            "address": i['address']
                        })
                    except:
                        continue
                return render_template("vhelp.html", hospitals=hospitals, location=location)
            else:
                return render_template("vhelp.html", error="Location not found", location=location)
        else:
            return render_template("vhelp.html", error="Please provide a location", location='')
    return render_template("vhelp.html", location='', error='')

if __name__ == "__main__":
    app.run(debug=True)
