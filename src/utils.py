import bs4

import subprocess

async def get_vid(video):
    return subprocess.check_output(["yt-dlp", "--no-warnings", "-f", "best/bestvideo+bestaudio", "--get-url", video])
