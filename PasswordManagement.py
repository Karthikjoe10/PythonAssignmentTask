
import re

# Decorator to log validation status
def log_validation(func):
    def wrapper(password):
        errors = func(password)

        if len(errors) == 0:
            print("Password validation successful!")
        else:
            print("Password validation failed!")

        return errors

    return wrapper


# Function to validate password
@log_validation
def validate_password(password):

    errors = []

    # Check minimum length
    if len(password) < 8:
        errors.append("at least 8 characters")

    # Check uppercase letter
    if not re.search(r"[A-Z]", password):
        errors.append("uppercase letter")

    # Check lowercase letter
    if not re.search(r"[a-z]", password):
        errors.append("lowercase letter")

    # Check digit
    if not re.search(r"[0-9]", password):
        errors.append("digit")

    # Check special character
    if not re.search(r"[@#$]", password):
        errors.append("special character (@, #, $)")

    return errors


# Main program
while True:

    try:
        password = input("\nEnter password: ")

        errors = validate_password(password)

        if len(errors) == 0:
            print("Password is valid!")
            break

        else:
            print("\nPassword is invalid.")

            for error in errors:
                print("Missing:", error)

    except Exception as e:
        print("Error:", e)
