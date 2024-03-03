from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

# 대분류 chapter 단위
class chapter(BaseModel):
    chapter_id: int
    created_at: datetime
    updated_at: datetime

# chapter 안에 stage
class stage(BaseModel):
    stage_id: int
    created_at: datetime
    updated_at: datetime

# 재화 관련 DB
class items(BaseModel):
    coin: int
    heart: int
