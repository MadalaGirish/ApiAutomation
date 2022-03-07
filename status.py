import requests

def test_status():
 resp=requests.get("https://hbs-ob-stage.herokuapp.com/status")
 print(resp)