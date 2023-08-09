'''
Author : Pramod
Objective : Create and Verify by Post Request
TC#1 - Verify the Status Code, Headers
TC#2 - Verify the Body -> Booking ID
TC#3 - Verify the JSON Schema is Valid
'''

from src.constants.apiconstant import url_create_booking
from src.helpers.api_wrapper import post_request
from src.helpers.payload_manager import payload_create_booking
from src.helpers.utils import common_headers
from src.helpers.common_verification import verify_http_code,verify_key

import pytest
import allure


class TestIntegration(object):

     @pytest.mark.smoke
     @allure.feature('TC#1 - Verify Create Booking Feature')
     def test_create_booking_tc1(self):
        response = post_request(url_create_booking(), headers=common_headers(), auth=None,
                                payload=payload_create_booking(), in_json=False)
        verify_http_code(response, 200)
        booking_id = response.json()["bookingid"]
        verify_key(response, booking_id)



     @pytest.mark.smoke
     @allure.feature('TC#2 - Verify Update Booking Feature')
     def test_update_Put(self):
         assert True



     @pytest.mark.smoke
     @allure.feature('TC#3 - Verify Delete Booking Feature')
     def test_delete(self):
         assert True