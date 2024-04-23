from fastapi import FastAPI
from app.api.core import views

app = FastAPI()

# Incluye las vistas definidas en mutant.py
app.include_router(views.router)
