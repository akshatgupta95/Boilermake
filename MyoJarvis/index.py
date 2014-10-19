# require("/Users/Dhruv/twilio-node/lib");


# var accountSid = 'AC7d542add18f47cedfa9e1f82f226fc62';
# var authToken = "1b6b4e76b8950e8634a3675f77129b06";
# var client = require('twilio')(accountSid, authToken);
 
# client.sendMessage({

#     to:'+12178197556', // Any number Twilio can deliver to
#     from: '+17159524016', // A number you bought from Twilio and can use for outbound communication
#     body: 'Test Message' // body of the SMS message

# }, function(err, responseData) { //this function is executed when a response is received from Twilio

#     if (!err) { // "err" is an error received during the request, if any

#         console.log(responseData.from); // outputs "+14506667788"
#         console.log(responseData.body); // outputs "word to your mother."

#     }
# });

# import urllib2
# urllib2.urlopen("http://example.com/foo/bar").read()

# https://api.venmo.com/v1/payments/4?access_token=<access_token>

from flask import Flask,render_template
from twilio.rest import TwilioRestClient

app = Flask(__name__)

@app.route("/")
def index():
	account_sid = "AC7d542add18f47cedfa9e1f82f226fc62"
	auth_token  = "1b6b4e76b8950e8634a3675f77129b06"
	client = TwilioRestClient(account_sid, auth_token	)
	message = client.messages.create(body="Jenny please?! I love you <3",
    to="+14252098743",    # Replace with your phone number
    from_="+17159524016") # Replace with your Twilio number
	print message.sid


	return render_template('index.html')


 
# Your Account Sid and Auth Token from twilio.com/user/account


# @app.route("/money")
# def money():
#     #account_sid = "AC7d542add18f47cedfa9e1f82f226fc62"
#     account_sid = "AC7d542add18f47cedfa9e1f82f226fc62"
# 	auth_token  = "1b6b4e76b8950e8634a3675f77129b06"
# 	client = TwilioRestClient(account_sid, auth_token	)
# 	message = client.messages.create(body="Haha", to="+12178197557",from_="+17159524016") # Replace with your Twilio number

# print message.sid
# return None
# account_sid = "AC7d542add18f47cedfa9e1f82f226fc62"
# auth_token  = "1b6b4e76b8950e8634a3675f77129b06"
# client = TwilioRestClient(account_sid, auth_token	)
# message = client.messages.create(body="Haha",
 #    to="+12178197557",    # Replace with your phone number
 #    from_="+17159524016") # Replace with your Twilio number
# print message.sid



if __name__ == "__main__":
    app.run()