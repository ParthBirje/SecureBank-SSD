import logging

# SecureBank: input validation and controlled error handling

# Configure centralized logging
logging.basicConfig(
    filename="securebank.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def process_login(username, password):
    try:
        if not username or not password:
            logging.warning("Login validation failed")
            return "Invalid login details. Please try again."

        if username == "admin" and password == "1234":
            logging.info("Successful login for user: admin")
            return "Login successful."

        logging.warning("Failed login attempt")
        return "Invalid login details. Please try again."

    except Exception:
        logging.error("Unexpected application error")
        return "Something went wrong. Please try again."


print("=== SecureBank Login ===")

username = input("Enter username: ")
password = input("Enter password: ")

message = process_login(username, password)

print("Message:", message)