# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACe8cb0d335696f3408f92a708103abfce'
auth_token = '4744827cb6df07b7422bee4e2d761972'
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         from_='whatsapp:+14155238886',
         body="It's taco time!",
         to='whatsapp:+34661981581'
     )

print(message.sid)
