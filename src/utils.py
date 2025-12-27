import subprocess
import os

async def get_vid(video):
    if os.path.isfile("config/cookies.txt"):
        print("cookie")
        return subprocess.check_output(["yt-dlp", "--cookies", "config/cookies.txt", "--no-warnings", "-f", "best/bestvideo+bestaudio", "--get-url", video])
    else:
        return subprocess.check_output(["yt-dlp", "--no-warnings", "-f", "best/bestvideo+bestaudio", "--get-url", video])

