import requests

def test_Edit_user():
    payload ={
    "name": "Girish",
    "phone": "+919040241401",
    "email": "user@hashedin.com",
    "password": "admin",
    "otp": 111111
}
    user="https://hbs-ob-stage.herokuapp.com/user"
    response = requests.put(url=user,json=payload)
    print(response)
    print(response.json())
