from flask import Flask, json,render_template,request
import requests
import http.client

app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def index():

    ipp = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    url = 'http://ip-api.com/json/'.format(ipp)
    req = requests.get(url)
    response = json.loads(req.text)
    city = response['city']
    city2 = str(city)

    conn = http.client.HTTPSConnection("api.collectapi.com")
    headers = {
    'content-type': "application/json",
    'authorization': "apikey 7qMYttsLt8n29p0NlalYd9:7vdi76VfE3Cr6SZevJHkhA"
    }

    conn.request("GET", "/weather/getWeather?data.lang=tr&data.city="+city2, headers=headers)
    res = conn.getresponse()
    data = json.loads(res.read())
    return render_template("index.html",res=data,city = city2)



@app.route("/hakkimda")
def hakkimda():
    return render_template("hakkimda.html")

if __name__ == "__main__":
    app.run(debug=True)