from utilities.api import api_is_up

if api_is_up():
    print("api looks good")
else:
    print("api looks bad")
