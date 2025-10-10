import re
import json

def is_valid_email(email):
    """Check if the email is a valid format."""
    # A robust regular expression for validating an Email
    regex = r"^[a-zA-Z0-9_.+-]+@(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}$"
    if re.match(regex, email):
        return True
    else:
        return False

if __name__ == "__main__":
    with open('email.json') as f:
        data = json.load(f)
    email_to_verify = data['email']

    if is_valid_email(email_to_verify):
        print(f"The email '{email_to_verify}' is valid.")
    else:
        print(f"The email '{email_to_verify}' is invalid.")