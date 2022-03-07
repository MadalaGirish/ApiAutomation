import requests

def test_Authenticate():
    payload = {
    "phone": "+919040241401",
    "LoginType": "OTP",
    "otp": "111111"
    }
    post = "https://hbs-ob-stage.herokuapp.com/authenticate"
    response = requests.post(url=post, json=payload)
    print(response)
    print(response.json())
