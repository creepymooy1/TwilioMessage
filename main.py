#send out messages using twilio API

import os
from twilio.rest import Client

# Twilio account credentials
account_sid = "sid here"  # Your Twilio Account SID
auth_token = "auth here"  # Your Twilio Auth Token

# Create a Twilio client object
client = Client(account_sid, auth_token)

# Compose the message and send it
message = client.messages.create(
    body="hello world",  # The content of the message
    from_="+18556409844",  # Your Twilio phone number
    to="+number here"  # The recipient's phone number
)

# Print the message SID (a unique identifier)
print(message.sid)
