import importlib
from fastapi import FastAPI

app = FastAPI()
url_module = importlib.import_module("app.api.urls")