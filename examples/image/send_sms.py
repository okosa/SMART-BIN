
from twilio.rest import Client

account_sid = "AC4bf9797897b1b61c525061a556cebcf3"
auth_token  = "f3be6123b7458194e8d70b12cd07846c"

client = Client(account_sid, auth_token)

myTwilioNumber = "+13345390541"
destCellPhone  = "+14036067666"

def send_text(message):
       
    if message == 3.5:
        yo = "Recycle"
    elif message == 5.8:
        yo = "Metal"
    elif message == 8.2:
        yo = "Compost"
    else:
        yo = "Other"
    
    myMessage = client.api.account.messages.create(
        body=yo + " is full",
        to=destCellPhone, 
        from_=myTwilioNumber)


