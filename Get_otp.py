import requests

def test_Otp():
    payload = {
        "phone": "+919040241401"
    }
    post = "https://hbs-ob-stage.herokuapp.com/get_register_otp"
    response = requests.post(url=post, json=payload)
    print(response.status_code)
    print(response.json())
