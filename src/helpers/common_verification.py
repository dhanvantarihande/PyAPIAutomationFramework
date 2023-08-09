def verify_http_code(response_data, expected_data):
    assert response_data.status_code == (expected_data),"Expected HTTP Status : " + expected_data

# Any Key should not be Null(empty)

def verify_key(response_data, key):
    assert key != 0, "Key is non Empty : " + key
    assert key > 0, "Key should be greater than zero : " + key