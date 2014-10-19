from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC7d542add18f47cedfa9e1f82f226fc62"
auth_token  = "1b6b4e76b8950e8634a3675f77129b06"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="Jenny please?! I love you <3",
    to="+14252098743",    # Replace with your phone number
    from_="+17159524016") # Replace with your Twilio number
print message.sid