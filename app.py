from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from utils import fetch_reply


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')
    phone_num = request.form.get('From')
    reply = fetch_reply(msg, phone_num)


    # Create reply
    resp = MessagingResponse()
    resp.message(reply)
    #resp.message("You said: {}".format(msg) + " nothing you have to see")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)