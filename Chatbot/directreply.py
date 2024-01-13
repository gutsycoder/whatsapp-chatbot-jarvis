import requests
import wikipedia
import json
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
api_request=requests.get("https://corona.lmao.ninja/countries")
api=json.loads(api_request.content)
app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])

def sms_ahoy_reply():
    c=0

    """Respond to incoming messages with a friendly SMS."""
    # Start our response
    body = request.form['Body']
    # Start our TwiML response
    resp = MessagingResponse()
    print(body)
    if ("Hi"  in body):
        resp.message("Hello Sir/Mam")
    if("name" in body):
        resp.message("You can call me as Jarvis")
    if ("Hello"  in body):
        resp.message("Hello Sir/Mam")
    if ("Bye" in body):
        resp.message("Bye Sir/Mam")
    if "What's up" in body:
        resp.message("I'm doing fine sir/mam .What about you?")
    if "fine" in body:
        resp.message("Pleased to know that sir/mam !")

    for i in range(0,183):
        if body==api[i]["country"]:
            resp.message(str(api[i]["country"]))
            resp.message("Confirmed Cases "+str(api[i]["cases"]))
            c=1
    if(c==0):
        resp.message(wikipedia.summary(body,sentences=2))




    # Determine the right reply for this message


    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
