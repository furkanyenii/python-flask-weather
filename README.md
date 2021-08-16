# Flask Weather App (Python)
 This project is a Flask (Python) application that automatically detects local weather based on user's external IP address. 
![screenshot](https://user-images.githubusercontent.com/37777649/129538005-e5f5b655-03b6-47f0-a4c3-85edad4e2029.png)
> Example screenshot of application

# Functionality
Gets a user's external IP address and then used http://ip-api.com to get more specific location information to pass into Weather API (https://collectapi.com/tr). Weather information is returned based on the location associated with the IP.

- To work on this locally clone the repo, request and add an API key (locally) from collectapi and then run app.py
- index.html displays weather information and displays the appropriate weather icon based on the current weather.


#### This App Provides us          
+ The Temperature
    * Max Temperature
    * Min Temperature
    * Night Temperature
+ Humidity
+ weather condition
+ 5 days weather forecast 
