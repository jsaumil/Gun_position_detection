# import subprocess
# import time

# # Define the commit message-
# commit_message = "Updated all files"

# def push_changes():
#     try:
#         # Stage all files
#         subprocess.run(["git", "add", "."], check=True)

#         # Commit the changes
#         subprocess.run(["git", "commit", "-m", commit_message], check=True)

#         # Push the changes
#         subprocess.run(["git", "push"], check=True)

#         print("All files successfully pushed to the repository!")
#     except subprocess.CalledProcessError as e:
#         print(f"An error occurred: {e}")

# # Run the push every minute
# try:
#     print("Auto-push started. Press Ctrl+C to stop.")
#     while True:
#         push_changes()
#         time.sleep(30)# Wait for 1 minute
# except KeyboardInterrupt:
#     print("Auto-push stopped.")

import subprocess
import time

# Define the commit message
commit_message = "Updated all files"

def pull_changes():
    try:
        # Pull the latest changes from the repository
        print("Pulling the latest changes from the repository...")
        subprocess.run(["git", "pull"], check=True)
        print("Successfully pulled the latest changes.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while pulling: {e}")

def push_changes():
    try:
        # Pull the latest changes first
        pull_changes()

        # Stage all files
        subprocess.run(["git", "add", "."], check=True)

        # Commit the changes
        subprocess.run(["git", "commit", "-m", commit_message], check=True)

        # Push the changes
        subprocess.run(["git", "push"], check=True)

        print("All files successfully pushed to the repository!")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

# Run the pull and push process every 30 seconds (adjust as needed)
try:
    print("Auto-push started. Press Ctrl+C to stop.")
    while True:
        push_changes()
        time.sleep(30)  # Wait for 30 seconds before the next push (adjust as needed)
except KeyboardInterrupt:
    print("Auto-push stopped.")
    