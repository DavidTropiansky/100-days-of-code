#Sending the text message

import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = '*****************************'
auth_token = '*****************************'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              from_='+YOUR TWILIO NUMBER',
                              body=message,
                              to='+YOUR PHONE NUMBER'
                          )

#end