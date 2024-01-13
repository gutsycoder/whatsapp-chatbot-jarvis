# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACe2403efde07fbd2931759bd31a5f1b3f'
auth_token = '8d5f07c318bf3da7fa740a18c24539c9'
client = Client(account_sid, auth_token)
value={"whatsapp:+919621810654","whatsapp:+918693826816","whatsapp:+919044652295","whatsapp:+918004860375","whatsapp:+917007265181","whatsapp:+919453970038"}
for i in value:
    message = client.messages.create(

                              body='Your twilio code is Send message to Suyash',
                              from_='whatsapp:+14155238886',
                              to=i
                          )

print(message.sid)
