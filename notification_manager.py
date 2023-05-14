from twilio.rest import Client

TWILIO_SID = "your Twilio account SID"
TWILIO_AUTH_TOKEN = "your Twilio auth token"
TWILIO_VIRTUAL_NUMBER = "your Twilio number "
TWILIO_VERIFIED_NUMBER = "your number that you used to sign in to Twilio"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )

