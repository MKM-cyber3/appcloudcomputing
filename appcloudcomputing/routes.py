import requests
import json
from isodate import parse_duration
from flask import Blueprint, render_template, current_app, request

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('home.html')

@main.route('/youtube', methods=['GET', 'POST'])
def index():

    search_url='https://www.googleapis.com/youtube/v3/search'
    video_url='https://www.googleapis.com/youtube/v3/videos'

    videos = []
    
    if request.method == 'POST':
        search_params={
            'key' :current_app.config['YOUTUBE_API_KEY'], 
            'q' :request.form.get('query'), 
            'part':'snippet', 
            'maxResults' :9,
            'type' :'video'
        }

        r=requests.get(search_url, params=search_params)
        #print(r.text)
        
        results=r.json()['items']

        #facem lista de id-uri video
        video_ids=[]
        for result in results:
            video_ids.append(result['id']['videoId'])

        video_params = {
            'key':current_app.config['YOUTUBE_API_KEY'],
            'id':','.join(video_ids),
            'part':'snippet,contentDetails',
            'maxResults':9
        }
    
        r=requests.get(video_url,params=video_params)
        results=r.json()['items']

        
        for result in results:
            video_data={
                'id' : result['id'],
                'url' : f'https://www.youtube.com/watch?v={ result["id"] }',
                'thumbnail' : result['snippet']['thumbnails']['high']['url'],
                'duration' : int(parse_duration(result['contentDetails']['duration']).total_seconds() // 60),
                'title' : result['snippet']['title'],
            }
            videos.append(video_data)

    return render_template('index.html', videos=videos)


@main.route('/weather',methods=['GET','POST'])
def weather():
    if request.method == 'POST':
        #weather_data = []
        #url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=271d1234d3f497eed5b1d80a07b3fcd1'
        city_name=request.form['city_name']
        #r=request.get(url.format(city)).json()
        

        url = "https://community-open-weather-map.p.rapidapi.com/weather"
        querystring = {"callback":"test","id":"2172797","units":"%22metric%22 or %22imperial%22","mode":"xml%2C html","q":f"{city_name}"}

        headers = {
            'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
            'x-rapidapi-key': "af5a0e595emshea6a102935e0127p11aa19jsnccc56be2a924"
            }

        response = requests.request("GET", url, headers=headers, params=querystring)

        #extract the json from string
        json_string = response.text.split("test(")[1]
        json_string= json_string.split(")")[0]

        #transform to json type
        json_value=json.loads(json_string)

        #get the elements from json 
    
        #vreme = []
        #rezultate = json_value['items']

        '''for rezultat in rezultate
            vreme_data= {
                'lat': rezultat['coord']['lat']
            }
            vreme.append(vreme_data)

        return render_template('weather.html', weather=vreme)'''

        return render_template('weather.html', weather=json_value['weather'][0]['description'])
    else :
         return render_template('weather.html')