import pytest
import requests

# Run this script multiple times
# Read the data from the excel file
# Pass the data one by one and run the function(test_make_auth_request) , How many rows in the excel file


def test_make_auth_request():
    payload = {
        "username": "admin",
        "password": "password123"
    }
    headers = {
        "Content-Type": "application/json",
    }
    response = requests.post("https://restful-booker.herokuapp.com/auth", headers=headers, json=payload)
    assert response.status_code == 200
    print(response.text)
    print(response.json()["token"])

