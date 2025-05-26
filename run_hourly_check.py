# run_hourly_check.py
# Place this file in your project root, same directory as manage.py

import subprocess
import time
import os
from datetime import datetime

# When running INSIDE an activated virtual environment, 'python' in the PATH
# already points to the venv's python.
# Also, 'manage.py' is usually found relative to the script's location.

PYTHON_EXECUTABLE = 'python' # Simply 'python' because venv is activated
MANAGE_PY_PATH = 'manage.py' # Relative path is fine from project root

# Define the Django management command to run
DJANGO_COMMAND = 'check_efficiency'

# Define the interval in seconds (e.g., 60 minutes * 60 seconds/minute = 3600 seconds for hourly)
CHECK_INTERVAL_SECONDS = 60 * 60 # 1 hour

def run_django_command():
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Executing Django command: {DJANGO_COMMAND}...")
    try:
        # Use subprocess.run to execute the Django command
        result = subprocess.run(
            [PYTHON_EXECUTABLE, MANAGE_PY_PATH, DJANGO_COMMAND],
            capture_output=True,
            text=True,
            check=True,
            cwd=os.path.dirname(os.path.abspath(__file__)) # Ensure it runs from the project root
        )
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Command output:\n{result.stdout}")
        if result.stderr:
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Command errors:\n{result.stderr}")
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Command '{DJANGO_COMMAND}' completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] ERROR: Command '{DJANGO_COMMAND}' failed with exit code {e.returncode}")
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] STDOUT:\n{e.stdout}")
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] STDERR:\n{e.stderr}")
    except FileNotFoundError:
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] ERROR: '{PYTHON_EXECUTABLE}' or '{MANAGE_PY_PATH}' not found. Ensure script is run from project root and venv is activated.")
    except Exception as e:
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] An unexpected error occurred: {e}")

if __name__ == '__main__':
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Starting continuous Django command runner loop...")
    while True:
        run_django_command()
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Waiting for {CHECK_INTERVAL_SECONDS} seconds before next run...")
        time.sleep(CHECK_INTERVAL_SECONDS)