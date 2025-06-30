import yt_dlp
import os

# Make sure the folder exists
output_folder = 'C:/Users/Andrei/Downloads'
os.makedirs(output_folder, exist_ok=True)

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': output_folder + '/%(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

video = input('What video would you like to download? ')

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download(
        [video])
