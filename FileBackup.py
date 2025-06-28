# modules that will be used
import shutil
import os
from datetime import datetime
import schedule
import time

# directories
backup = 'C:/Backups'
source = "C:/Vaults/Vault1"

# Create timestamped backup folder path
now = datetime.now()
timestamp = now.strftime("%Y-%m-%d")
backup_folder = os.path.join(backup, 'Brain_Backup-' + timestamp)


# scheduleing the daily backups
schedule.every().day.at("20:00").do(
    lambda: shutil.copytree(source, backup_folder))


# making the code run 24/7
while True:
    schedule.run_pending()
    time.sleep(60)
  
