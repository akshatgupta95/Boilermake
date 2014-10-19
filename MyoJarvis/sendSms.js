require("/Users/Akshat/twilio-node/lib");

var accountSid = 'AC7d542add18f47cedfa9e1f82f226fc62';
var authToken = "1b6b4e76b8950e8634a3675f77129b06";
var client = require('twilio')(accountSid, authToken);
 
client.sendMessage({

    to:'+12178197556', // Any number Twilio can deliver to
    from: '+17159524016', // A number you bought from Twilio and can use for outbound communication
    body: 'Test Message' // body of the SMS message

}, function(err, responseData) { //this function is executed when a response is received from Twilio

    if (!err) { // "err" is an error received during the request, if any

        console.log(responseData.from); // outputs "+14506667788"
        console.log(responseData.body); // outputs "word to your mother."

    }
});

