import os

from dotenv import load_dotenv

import dotenv
import pytest
import requests





@pytest.fixture
def test_post_create_Booking():
    payload_create_booking = {
    "firstname" : "Jim",
    "lastname" : "Brown",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"
    }

    headers = {
        "Content-Type": "application/json",
    }
    response = requests.post("https://restful-booker.herokuapp.com/booking",headers=headers,
                             json= payload_create_booking)
    print(response.json())
    booking_id = response.json()["bookingid"]
    print(booking_id)
    print(response.headers)
    assert response.status_code == 200
    return booking_id


def test_put_req(test_post_create_Booking):
    payload_create_booking = {
    "firstname" : "Reyansh",
    "lastname" : "Hande",
    "totalprice" : 1337,
    "depositpaid" : False,
    "bookingdates" : {
        "checkin" : "2024-01-01",
        "checkout" : "2024-01-01"
    },
    "additionalneeds" : "Breakfast, Lunch"
    }
    load_dotenv()
    temp_token = "token=" + os.getenv("token")
    print(temp_token)
    headers = {
        "Content-Type": "application/json",
        "Cookie" : temp_token
    }
    url_put = "https://restful-booker.herokuapp.com/booking/" + str(test_post_create_Booking)
    response = requests.put(url_put, headers=headers,
                            json=payload_create_booking)
    print(response.text)
    print(response.status_code)
    assert response.status_code == 403

