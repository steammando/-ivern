from fastapi import FastAPI
from pydantic import BaseModel
from .domain.gatcha import element_gatcha, parts_gatcha, gatcha_n_times
from .domain.chapter import chapter_start, chapter_clear, stage_start, stage_clear
from core.sheet import open_sheet, read_all_sheet
import datetime
from typing import List, Optional


tags_metadata = [
    {"name": "gatcha", "description": "가챠 메소드"},
    {"name": "chapter", "description": "챕터와 스테이지 관련 메소드"},
    {"name": "item", "description": "아이템 및 보상관련 메소드(@todo payments)"},
    {"name": "operation", "description": "내부 동작용 메소드"},
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
@app.post("/chapter/start/v1/{user_id}/{chapter_id}", tags=['chapter'])
async def chapter_start(user_id: int, chapter_id: int):
    result = {}
    result['user_id'] = user_id
    result['chapter_id'] = chapter_id
    result['created_at'] = datetime.datetime.utcnow()
    result['updated_at'] = datetime.datetime.utcnow()
    return result
    # return chapter_start(int(chapter_id))

# chapter clear api
@app.post("/chapter/clear/v1/{user_id}/{chapter_id}", tags=['chapter'])
async def chapter_clear(user_id: int, chapter_id: int):
    result = {}
    result['user_id'] = user_id
    result['chapter_id'] = chapter_id
    result['created_at'] = datetime.datetime.utcnow()
    result['updated_at'] = datetime.datetime.utcnow()
    return result
    # return chapter_clear(int(chapter_id))

# stage start api
@app.post("/stage/start/v1/{user_id}/{chapter_id}/{stage_id}", tags=['chapter'])
async def stage_start(user_id: int, stage_id: int, chapter_id: int):
    result = {}
    result['user_id'] = user_id
    result['chapter_id'] = chapter_id
    result['stage_id'] = stage_id
    result['created_at'] = datetime.datetime.utcnow()
    result['updated_at'] = datetime.datetime.utcnow()
    return result
    # return stage_start(int(chapter_id), int(stage_id))

# stage clear api
@app.post("/stage/clear/v1/{user_id}/{chapter_id}/{stage_id}/{coin}", tags=['chapter'])
async def stage_clear(user_id: int,  stage_id: int, chapter_id: int, coin: int):
    result = {}
    result['user_id'] = user_id
    result['chapter_id'] = chapter_id
    result['stage_id'] = stage_id
    result['created_at'] = datetime.datetime.utcnow()
    result['updated_at'] = datetime.datetime.utcnow()
    result['coin'] = coin
    return result
    # return stage_clear(int(chapter_id), int(stage_id))

@app.get("/get/stage/v1/{user_id}", tags=['chapter'])
async def get_stage(user_id: int):
    result = []
    result['user_id'] = user_id
    result['current_chapter'] = 1
    result['current_stage'] = 2
    return result

@app.get("/sheet/v1/", tags=['operation'])
async def get_sheet(sheet_name: Optional[str] = None):
    if sheet_name:
        result = open_sheet(sheet_name)
    else:
        result = read_all_sheet()
    return result

@app.get("/get/reward/v1/{user_id}", tags=['item'])
async def get_reward(user_id: int):
    result = {}
    # reward = open_sheet('items')[0]
    reward = 'heart'
    result['user_id'] = user_id
    result['item'] = reward
    result['cnt'] = 3

    result['current_item'] = {"heart":10, "continue":1}
    return result

@app.get("/get/stat/v1/{user_id}", tags=['stat'])
async def get_stat(user_id: int):
    result = {}
    # reward = open_sheet('items')[0]
    reward = 'heart'
    result['user_id'] = user_id
    result['health'] = 0
    result['attack_count'] = 1
    result['attack_speed'] = 2
    result['move_speed'] = 0
    result['projectile_speed'] = 1
    result['projectile_scale'] = 2

    return result

@app.post("/update/stat/v1/{user_id}/{stat}", tags=['stat'])
async def update_stat(user_id: int, stat: str):
    result = {}
    # reward = open_sheet('items')[0]
    reward = 'heart'
    result['user_id'] = user_id
    result['health'] = 1
    result['attack_count'] = 1
    result['attack_speed'] = 2
    result['move_speed'] = 0
    result['projectile_speed'] = 1
    result['projectile_scale'] = 2

    return result

@app.post("/reset/stat/v1/{user_id}", tags=['stat'])
async def reset_stat(user_id: int):
    result = {}
    # reward = open_sheet('items')[0]
    # reward = 'heart'
    result['user_id'] = user_id
    result['health'] = 0
    result['attack_count'] = 0
    result['attack_speed'] = 0
    result['move_speed'] = 0
    result['projectile_speed'] = 0
    result['projectile_scale'] = 0

    return result

@app.get("/login/{device_id}", tags=['login'])
async def login(device_id: str):
    result = {}
    user_id = 1
    result['user_id'] = 1
    
    return result