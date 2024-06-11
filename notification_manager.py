from twilio.rest import Client

TWILIO_SID = "ACab180f51808e1697d6f7dec5dc1f6ad3"
TWILIO_AUTH_TOKEN = "1ccdef2aa0170554df3d2593a3ced30b"
TWILIO_VIRTUAL_NUMBER = "+14583022639"
TWILIO_VERIFIED_NUMBER = "+919602993072"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )

        print(message.sid)