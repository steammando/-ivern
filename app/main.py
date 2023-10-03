from fastapi import FastAPI
from pydantic import BaseModel
from .domain.gatcha import weighted_gatcha, rated_gatcha
from .domain.chapter import chapter_start, chapter_clear, stage_start, stage_clear
from core.sheet import open_sheet, read_all_sheet
from app.db.models import chapter, stage, items, sheet
import datetime
from typing import List, Optional

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/gatcha/parts")
async def gatcha_parts():
    result = {}
    element = weighted_gatcha()
    parts = rated_gatcha()

    result['parts'] = parts
    result['element'] = element
    return result

# 가챠 테스트코드
@app.get("/gatcha/100")
async def gatch_100():
    p = {}
    e = {}
    result = []
    for i in range(100):
        parts = str(rated_gatcha())
        if parts in p:
            p[parts] += 1
        else:
            p[parts] = 1

        element = str(weighted_gatcha())
        if element in e:
            e[element] += 1
        else:
            e[element] = 1
    result.append(p)
    result.append(e)
    
    return result

# chapter start api
@app.post("/chapter/start/v1/{chapter_id}")
async def chapter_start(chapter_id: int):
    result = {}
    result['chapter_id'] = chapter_id
    result['created_at'] = datetime.datetime.utcnow()
    result['updated_at'] = datetime.datetime.utcnow()
    return result
    # return chapter_start(int(chapter_id))

# chapter clear api
@app.post("/chapter/clear/v1/{chapter_id}")
async def chapter_clear(chapter_id: int):
    result = {}
    result['chapter_id'] = chapter_id
    result['created_at'] = datetime.datetime.utcnow()
    result['updated_at'] = datetime.datetime.utcnow()
    return result
    # return chapter_clear(int(chapter_id))

# stage start api
@app.post("/stage/start/v1/{chapter_id}/{stage_id}")
async def stage_start(stage_id: int, chapter_id: int):
    result = {}
    result['chapter_id'] = chapter_id
    result['stage_id'] = stage_id
    result['created_at'] = datetime.datetime.utcnow()
    result['updated_at'] = datetime.datetime.utcnow()
    return result
    # return stage_start(int(chapter_id), int(stage_id))

# stage clear api
@app.post("/stage/clear/v1/{chapter_id}/{stage_id}/{coin}")
async def stage_clear(stage_id: int, chapter_id: int, coin: int):
    result = {}
    result['chapter_id'] = chapter_id
    result['stage_id'] = stage_id
    result['created_at'] = datetime.datetime.utcnow()
    result['updated_at'] = datetime.datetime.utcnow()
    result['coin'] = coin
    return result
    # return stage_clear(int(chapter_id), int(stage_id))

@app.get("/sheet/v1/")
async def get_sheet(sheet_name: Optional[str] = None):
    if sheet_name:
        result = open_sheet(sheet_name)
    else:
        result = read_all_sheet()
    return result