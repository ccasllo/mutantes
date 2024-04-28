import importlib
from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()
handler = Mangum(app)
url_module = importlib.import_module("app.api.urls")