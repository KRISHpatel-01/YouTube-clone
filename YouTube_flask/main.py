from flask import Flask, render_template, jsonify
import requests
from numerize.numerize import numerize

app=Flask(__name__)

Channels = {
    'Kurzgesagt' : 'UCsXVk37bltHxD1rDPwtNM8Q',
    'T-series' : 'UCq-Fj5jknLsUf-MWSy4_brA',
    'BBC' : 'UCN7B-QD0Qgn2boVH5Q0pOWg'
}

@app.route('/')
def home():
    
    url = "https://youtube138.p.rapidapi.com/channel/videos/"

    querystring = {"id":Channels['Kurzgesagt'],"hl":"en","gl":"US"}

    headers = {
        "X-RapidAPI-Key": "e13c598ecbmsh6d7fc8c16c1d686p1b6c3cjsn2556407ead8b",
        "X-RapidAPI-Host": "youtube138.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    
    data = response.json()
    content = data['contents']
    videos = [video['video'] for video in content if video['video']['publishedTimeText']]
    
    return render_template('index.html', videos=videos)

@app.template_filter()
def numberise(views):
    return numerize(views, 1)

@app.template_filter()
def image(thumbnails):
    return thumbnails[3]['url'] if len(thumbnails) >= 4 else thumbnails[0]['url']

app.run(host='0.0.0.0', port=81)