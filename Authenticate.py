import requests

def test_Authenticate():
    payload = {
    "phone": "+919040241401",
    "LoginType": "password",
    "password": "admin"
    }

    post = "https://hbs-ob-stage.herokuapp.com/authenticate"
    response = requests.post(url=post, json=payload)
    print(response.status_code)
    print(response.json())
