import logging
import os
from datetime import datetime

# Get current date components
now = datetime.now()
year = now.strftime("%Y")
month = now.strftime("%m_%B")  # Example: 03_March
day = now.strftime("%d")  # Example: 11

# Define the logs directory structure: logs/year/month/day/
logs_dir = os.path.join(os.getcwd(), "logs", year, month, day)
os.makedirs(logs_dir, exist_ok=True)  # Ensure all directories exist

# Generate log file name with timestamp
LOG_FILE = f"{now.strftime('%d_%b_%Y-%H.%M.%S')}.log"
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

logging.info("Logging setup complete.")