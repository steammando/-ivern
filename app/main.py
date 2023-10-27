from fastapi import FastAPI
from pydantic import BaseModel
from .domain.gatcha import element_gatcha, parts_gatcha, gatcha_n_times
from .domain.chapter import chapter_start, chapter_clear, stage_start, stage_clear
from core.sheet import open_sheet, read_all_sheet
from app.db.models import chapter, stage, items, sheet
import datetime
from typing import List, Optional


tags_metadata = [
    {"name": "gatcha", "description": "Gatcha APIs"},
    {"name": "item", "description": "Item APIs"},
    {"name": "chapter", "description": "Stage & Chapter APIs"},
    {"name": "operation", "description": "Operation APIs"},
    {"name": "test", "description": "Test APIs"},
]

app = FastAPI(openapi_tags=tags_metadata)


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/gatcha/1", tags=["gatcha"])
async def gatcha_parts():
    """
     가챠 1회
    """
    result = gatcha_n_times(1)
    return result

@app.get("/gatcha/10", tags=["gatcha"])
async def gatcha_10():
    """
     가챠 10회
    """
    result = gatcha_n_times(10)
    return result


# 가챠 테스트코드
@app.get("/gatcha/100/test", tags=['test'])
async def gatch_100():
    """
     (TEST API)가챠 100회했을 때 확률대로 잘 나오는지 테스트하는 API
    """
    p = {}
    e = {}
    result = []
    for i in range(100):
        parts = str(parts_gatcha())
        if parts in p:
            p[parts] += 1
        else:
            p[parts] = 1

        element = str(element_gatcha())
        if element in e:
            e[element] += 1
        else:
            e[element] = 1
    result.append(p)
    result.append(e)
    
    return result

# chapter start api
@app.post("/chapter/start/v1/{chapter_id}", tags=['chapter'])
async def chapter_start(chapter_id: int):
    result = {}
    result['chapter_id'] = chapter_id
    result['created_at'] = datetime.datetime.utcnow()
    result['updated_at'] = datetime.datetime.utcnow()
    return result
    # return chapter_start(int(chapter_id))

# chapter clear api
@app.post("/chapter/clear/v1/{chapter_id}", tags=['chapter'])
async def chapter_clear(chapter_id: int):
    result = {}
    result['chapter_id'] = chapter_id
    result['created_at'] = datetime.datetime.utcnow()
    result['updated_at'] = datetime.datetime.utcnow()
    return result
    # return chapter_clear(int(chapter_id))

# stage start api
@app.post("/stage/start/v1/{chapter_id}/{stage_id}", tags=['chapter'])
async def stage_start(stage_id: int, chapter_id: int):
    result = {}
    result['chapter_id'] = chapter_id
    result['stage_id'] = stage_id
    result['created_at'] = datetime.datetime.utcnow()
    result['updated_at'] = datetime.datetime.utcnow()
    return result
    # return stage_start(int(chapter_id), int(stage_id))

# stage clear api
@app.post("/stage/clear/v1/{chapter_id}/{stage_id}/{coin}", tags=['chapter'])
async def stage_clear(stage_id: int, chapter_id: int, coin: int):
    result = {}
    result['chapter_id'] = chapter_id
    result['stage_id'] = stage_id
    result['created_at'] = datetime.datetime.utcnow()
    result['updated_at'] = datetime.datetime.utcnow()
    result['coin'] = coin
    return result
    # return stage_clear(int(chapter_id), int(stage_id))

@app.get("/sheet/v1/", tags=['operation'])
async def get_sheet(sheet_name: Optional[str] = None):
    if sheet_name:
        result = open_sheet(sheet_name)
    else:
        result = read_all_sheet()
    return result