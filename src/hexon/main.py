from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from hexon.core.config import settings
from hexon.api.api_v1.api import api_router


hexon = FastAPI()

# Directory where your React build is located
react_build_directory = "static"

# Serve Static Files
hexon.mount("/static", StaticFiles(directory=react_build_directory), name="static")


@hexon.get("/")
def read_root():
    return FileResponse(f'{react_build_directory}/index.html')


hexon.include_router(api_router, prefix=settings.API_V1_STR)