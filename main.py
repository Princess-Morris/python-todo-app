import urllib
from routes.route import router
from fastapi import FastAPI

app = FastAPI()

app.include_router(router)