import requests

endpoint = "http://api.openweathermap.org/data/2.5/weather"
payload = {"q": "London,UK", "units":"metric", "appid":"ecbd08628615b6ce336f0dfd0d0c101f"}
response = requests.get(endpoint, params=payload)
print response.url
print response.status_code
print response.headers["content-type"]
data = response.json()
windspeed = data["wind"]["speed"]
name = data["name"]
weather = data["weather"][0]["main"]
print u"The windspeed is {}".format(windspeed)
print u"It's C in {}, and the sky is {}".format(name, weather)

