from twilio.rest import Client
import config

client = Client(config.account_sid, config.auth_token)

message = client.messages.create(
    messaging_service_sid=config.messaging_service_sid,
    body='This, is an sms test from Python. ',
    to=config.phone_number
)

print(message.sid)
