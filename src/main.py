import utils 

from typing import Annotated

import asyncio

from fastapi import FastAPI, Header, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import yt_dlp

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/watch")
async def main(request: Request, v: str, user_agent: Annotated[str | None, Header()] = None):
    video_str = "https://www.youtube.com/watch?v=" + v
    print(video_str)
    if user_agent.startswith("Mozilla"):
        return templates.TemplateResponse(
                request=request,name="watch.html", context={"link": video_str}
                )
    url = await utils.get_vid(video_str)
    await asyncio.sleep(4) # idk why but the first video slices dont work if playlist is immediately played so i added this sleep
    return RedirectResponse(url.decode("ascii"), status_code=302)
