from datetime import datetime
import os

import requests

'''
    # TODO: Implement log generation logic

    # STEP 1: Validate input
    # Hint: Check if data is a list

    # STEP 2: Generate a filename with today's date (e.g., "log_20250408.txt")
    # Hint: Use datetime.now().strftime("%Y%m%d")

    # STEP 3: Write the log entries to a file using File I/O
    # Use a with open() block and write each line from the data list
    # Example: file.write(f"{entry}\n")

    # STEP 4: Print a confirmation message with the filename
    # '''

def fetch_data():
    """
    Fetch sample data from a public API using the external requests package.
    """
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1", timeout=10)
    if response.status_code == 200:
        return response.json()
    return {}


def generate_log(data):
    if not isinstance(data, list): # STEP 1: Validate input
        raise ValueError("Input must be a list")

    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt" # STEP 2: Generate a filename with today's date

    with open(filename, "w", encoding="utf-8") as file: # STEP 3: Write the log entries to a file using File I/O
        for entry in data:
            file.write(f"{entry}\n")

    print(f"Log written to {filename}") # STEP 4: Print a confirmation message with the filename
    return filename


if __name__ == "__main__":
    log_data = ["User logged in", "User updated profile", "Report exported"]

    post = fetch_data()
    if post:
        log_data.append(f"Fetched Post Title: {post.get('title', 'No title found')}")

    generate_log(log_data)
    
