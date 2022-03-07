
from twilio.rest import Client

account_sid = "AC4bf9797897b1b61c525061a556cebcf3"
auth_token  = "f3be6123b7458194e8d70b12cd07846c"

client = Client(account_sid, auth_token)

myTwilioNumber = "+13345390541"
destCellPhone  = "+14036067666"

myMessage = client.api.account.messages.create(
    body="whatever",
    to=destCellPhone, 
    from_=myTwilioNumber)

