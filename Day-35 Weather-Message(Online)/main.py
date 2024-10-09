import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

'''

# To set environment variable use these commands in terminal
export AUTH_TOKEN=1basds9fd6xxxxxxxxxxxxxxxx8f; 
export MOB_NO=+91xxxxxxxx; 
export ACCOUNT_SID=AD2d8xxxxxxxxxxxxxxxxxxxx6f4d82; 
export OWM_API_KEY=9302xxx40adxxxxxxxxxxxxx8914c;

# Use this code to excess environment variable in OOP_Coffee_Machine.py
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
api_key = os.environ.get("OWM_API_KEY")
mob_no = os.environ.get("MOB_NO")

'''

account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
api_key = os.environ.get("OWM_API_KEY")
mob_no = os.environ.get("MOB_NO")

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"

LAT = 26.283340
LON = 73.021858

weather_parameter = {
    "lat": LAT,
    "lon": LON,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(url=OWM_Endpoint, params=weather_parameter)
response.raise_for_status()

weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {"https": os.environ["https_proxy"]}
    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an Umbrella.☔",
        from_='+12568184743',
        to=mob_no
    )
    print(message.status)
