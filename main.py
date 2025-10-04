import requests
from twilio.rest import Client

account_sid = "ACc2c329e8db45b50181096c0ce74f92ef"
auth_token = "b9c26bb925e1e732658ecb7e1f474ae2"
client = Client(account_sid, auth_token)

api_key = "13b2f6162343c490ec4342435137c647"
parameters = {
    "lat": 23.412138,
    "lon": 88.492645,
    "appid": api_key,
    "cnt": 4
}

OWM_endpoint = "http://api.openweathermap.org/data/2.5/forecast"
response = requests.get(url=OWM_endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()

#print(weather_data["list"][0]["weather"][0]["id"])
will_rain = False
for hour_data in weather_data["list"]:
    condition_code = (hour_data["weather"][0]["id"])
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        to='whatsapp:+919749022306',
        body="It's going to rain 🌧️ today\n. Remember to bring an☔"

    )
    print(message.status)