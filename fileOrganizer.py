import os
import shutil
import schedule
import time

# Directories
source = "C:/Users/Andrei/Downloads"  # where to take the files from
file_types = {
    "Music": [".mp3", ".wav"],
    "Videos": [".mp4", ".mov"],
    "Images": [".jpg", ".png", ".jpeg"],
    "Documents": [".pdf", ".txt", ".docx"],
}
# where to move them
destination_folders = {
    "Music": "C:/Users/Andrei/Music/",
    "Videos": "C:/Users/Andrei/Videos/",
    "Images": "C:/Users/Andrei/Images/",
    "Documents": "C:/Users/Andrei/Documents/",
}


# Main Function
def organize_files():
    # going into directory
    os.chdir(source)
    # taking the files from the directories
    files = os.listdir()

    for file in files:
        if os.path.isdir(file):
            continue

        # takes the extensions from the file
        ext = os.path.splitext(file)[1].lower()
        # checking if the fies contain one of the extensions
        for folder, extensions in file_types.items():
            if ext in extensions:
                # checks weather destination exists
                os.makedirs(destination_folders[folder], exist_ok=True)
                destination_path = os.path.join(
                    destination_folders[folder], file)
                # moves the file to the destination
                shutil.move(file, destination_path)
                break


# Schedule the task every 10 seconds
schedule.every(10).seconds.do(organize_files)

print("Organizer running...")

# Keep the script alive
while True:
    schedule.run_pending()
    time.sleep(1)
