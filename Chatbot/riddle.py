from itertools import permutations
import enchant
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])

def sms_ahoy_reply():
    body = request.form['Body']
    # Start our TwiML response
    resp = MessagingResponse()
    per=permutations(body)
    d = enchant.Dict("en_US")
    for i in per:
        if(d.check(''.join(i))):
            resp.message(''.join(i))
    
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
