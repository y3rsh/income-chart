# /// script
# requires-python = "==3.13.*"
# ///

import subprocess
from datetime import datetime


def commit_and_push():

    # Add all files to Git
    subprocess.run(["git", "add", "--all"], check=True)

    # Generate commit message with timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    commit_message = f"📊 Update 📈 {timestamp} ✏️"

    # Commit changes
    subprocess.run(["git", "commit", "-m", commit_message], check=True)

    # Push changes
    subprocess.run(["git", "push"], check=True)


if __name__ == "__main__":
    commit_and_push()
