import requests
def test_create_user():
    payload ={
        "name": "girish",
        "phone": "+919040241401",
        "email": "user1@hashedin.com",
        "password": "admin",
        "otp": 111111
    }
    print(type(payload))
    user="https://hbs-ob-stage.herokuapp.com/user"
    response = requests.post(url=user,json=payload)
    print(response)
    print(response.json())
