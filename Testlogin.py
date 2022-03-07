import requests
import json

def test_login():
 resp=requests.get("https://hbs-ob-stage.herokuapp.com/protected_test")
 print(resp)
 print(resp.headers.get("Content-Type"))
