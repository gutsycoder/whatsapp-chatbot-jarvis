# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
import requests
import json
api_request=requests.get("https://corona.lmao.ninja/countries")
api=json.loads(api_request.content)
account_sid = 'ACe2403efde07fbd2931759bd31a5f1b3f'
auth_token = '8d5f07c318bf3da7fa740a18c24539c9'
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body=str(api[42]),
         from_='+12074075765',
         to='+918299270301'
     )

print(message.sid)
