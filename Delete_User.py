import requests

def test_delete_user():
    payload ={
            "phone": "+919040241401",
            "otp": 111111
        }
    print(type(payload))
    user="https://hbs-ob-stage.herokuapp.com/user"
    response = requests.delete(url=user,json=payload)
    print(response)
    print(response.json())
