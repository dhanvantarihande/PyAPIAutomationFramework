# It is Just a Document File
# Python API Automation Framework

### Integration Test Cases for the Restful Booker
URL - https://restful-booker.herokuapp.com/apidoc/index.html

1. Verify GET, POST, PATCH, DELETE, PUT
2. Response Body,Headers, Status Code.
3. Auth - Basic Auth, Cookie Based Auth.
4. JSON Schema Validation



## Tech Stack (Python Packages used)
1. Python, Request Module
2. Pytest, Pytest-html
3. Allure Report
4. Faker, CSV, JSON, YAML.
5. Run Via Commandline - Jenkins


#### P.S - DB Connection(in Future)

## Install pip packages
- `pip install requests pytest pytest-html faker allure-pytest jsonschema`
- `pip install requirements.txt`

## How to run Locally and see the Report?
- ``pytest tests/* -s -v --alluredir=./reports --html=report.html``



## How to Run via Jenkins?#   P y A P I A u t o m a t i o n F r a m e w o r k  
 