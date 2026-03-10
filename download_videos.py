from yt_dlp import YoutubeDL
import os

def run():
    folder = input("Enter folder name(where video will save):")
    
    os.makedirs(folder, exist_ok=True)
    
    with open("streams.txt") as f:
        streams = [x.strip() for x in f.readlines() if x.strip()]
    
    for i, url in enumerate(streams, start=1):
    
        ydl_opts = {
            "outtmpl": f"{folder}/amazom_video{i}.%(ext)s"
    }
    
        try:
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
        except:
            print("Failed:", url)