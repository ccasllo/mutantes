from config.main import app
from fastapi import APIRouter
from app.api.v1 import views as api
urls = APIRouter()


# Meta URLs
@urls.get("/")
def root():
    """
    This api aims to assist Professor Charles Xavier in identifying mutants 
    based on their DNA sequences,in order to recruit them for his school 
    to combat the Sentinels. The API detects whether a person is a mutant
    by analyzing their DNA sequence.
    """
    return {'message': 'Mutantes ok'}


urls.include_router(api.router, prefix="/api/v1")


app.include_router(urls)
