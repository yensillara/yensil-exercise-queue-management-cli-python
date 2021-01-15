# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client

def send(body='Some body', to=''):
    # Your Account Sid and Auth Token from twilio.com/console
    # DANGER! This is insecure. See http://twil.io/secure
    account_sid = 'AC6ebec1df30d6476df7029db9ebe4e013'
    auth_token = '1505a1047cc7d2a2baeaffef285d07b3'
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body=body,
                        from_='+17279456359',
                        to='+'+to
                    )

    print(message.sid)