from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC7d542add18f47cedfa9e1f82f226fc62"
auth_token  = "1b6b4e76b8950e8634a3675f77129b06"
client = TwilioRestClient(account_sid, auth_token)
 
call = client.calls.create(url="http://demo.twilio.com/docs/voice.xml",
    to="+14252098743",
    from_="+17159524016")
print ("Calling")
