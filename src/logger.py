import logging
import os
from datetime import datetime

# Generate log file name with timestamp
LOG_FILE = f"{datetime.now().strftime('%d_%b_%Y-%H.%M.%S')}.log"

# Define logs directory
logs_dir = os.path.join(os.getcwd(), "logs")  # Only the directory path
os.makedirs(logs_dir, exist_ok=True)  # Create logs directory if it doesn't exist

# Define the full path of the log file
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

logging.info("Logging setup complete.")
