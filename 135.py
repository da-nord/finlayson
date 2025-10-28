import csv
import random
import time
import shutil
import logging
import os
from datetime import datetime

# Configuration
CSV_FILE = 'sales.csv'  # Path to the CSV file
#CSV_FILE = '135.csv'  # Path to the CSV file
BACKUP_DIR = 'backup/'   # Backup directory
BACKUP_INTERVAL = 10     # Time in seconds to wait between operations

# Setup logging
logging.basicConfig(filename='sales_shuffler.log', level=logging.INFO, 
                   format='%(asctime)s - %(levelname)s - %(message)s')

#logging.basicConfig(filename='135.log', level=logging.INFO, 
#                  format='%(asctime)s - %(levelname)s - %(message)s')

# Track today's backup status
backup_done = False
backup_date = None

def backup_file():
    global backup_done, backup_date
    today = datetime.now().date()
    
    # Check if backup is already done today
    if backup_done and backup_date == today:
        logging.info("Backup already done for today.")
        return

    try:
        shutil.copy(CSV_FILE, os.path.join(BACKUP_DIR, f'sales_backup_{today}.csv'))
        #shutil.copy(CSV_FILE, os.path.join(BACKUP_DIR, f'135{today}.csv'))
        logging.info("Backup created successfully.")
        backup_done = True
        backup_date = today
    except Exception as e:
        logging.error(f"Failed to backup file: {e}")

def shuffle_sales_data():
    try:
        with open(CSV_FILE, mode='r', newline='') as file:
            reader = list(csv.reader(file))
        
        # Shuffle the data (excluding header)
        header = reader[0]
        data = reader[1:]
        random.shuffle(data)
        
        # Write shuffled data back to the original CSV file
        with open(CSV_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(data)
        
        logging.info("Data shuffled successfully.")
    except Exception as e:
        logging.error(f"Error during data processing: {e}")

def main():
    while True:
        backup_file()
        shuffle_sales_data()
        time.sleep(BACKUP_INTERVAL)

if __name__ == "__main__":
    main()