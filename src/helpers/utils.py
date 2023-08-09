# This utils basically helps you to read the JSON files and provide you the JSON Data
import json


def get_payload_auth():
    # Read from the auth.json and return json
    file_data = open("src/resources/auth.json")
    data = json.loads(file_data)
    file_data.close()
    return data


def common_headers():
    headers = {
        "Content-Type": "application/json"
    }
    return headers