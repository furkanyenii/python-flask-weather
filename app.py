from flask import Flask, json,render_template,request,jsonify
import requests
app = Flask(__name__)

app.static_folder = 'static'

@app.route("/")
def index():
    #Kullanıcının konumunu bulan kod
    url = 'http://ip-api.com/json/'.format(request.remote_addr)
    r = requests.get(url)
    j = json.loads(r.text)
    city = j['city']
    city2 = str(city)

    url2 = 'https://www.metaweather.com/api/location/search/?query='+city2
    req = requests.get(url2)
    gelen = json.loads(req.text)
    woeid = gelen[0]['woeid'] 
    woeid2 = str(woeid)

    url3 = 'https://www.metaweather.com/api/location/'+woeid2
    req2 = requests.get(url3)
    gelen2 = json.loads(req2.text)


    return render_template("index.html",city = city,woeid = woeid,veri=gelen2)

@app.route("/hakkimda")
def hakkimda():
    return render_template("hakkimda.html")

if __name__ == "__main__":
    app.run(debug=True)