# Add your constants here

# Adding my URL constants

def base_url():
    # In future we can changed based on the env.json - Stage, Prepod, Production
    # If i want to run this on diff environment then i'll pass the (env) to change the url
    # In future i'll write a logic to change the base url based on the environment
    # We can changed the url
    return "https://restful-booker.herokuapp.com"

def url_create_booking():
    return "https://restful-booker.herokuapp.com/booking"

# .env-qa
# # qa - https://restful-booker.herokuapp.com/booking
# .env-stage
# # stage - https://restful-booker.herokuapp.com/booking
# .env-prod
# # prod - https://restful-booker.herokuapp.com/booking'


def url_create_token():
    return "https://restful-booker.herokuapp.com/auth"


def url_update_delete_booking(booking_id):
    return "https://restful-booker.herokuapp.com/booking/" + booking_id