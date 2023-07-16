from fastapi import FastAPI
from domain.gatcha import gatcha

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/sheet")
async def open_specific_sheet():
    result = gatcha()
    return result
