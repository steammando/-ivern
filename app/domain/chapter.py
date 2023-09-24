from datetime import timezone
import datetime
  
  
# Getting the current date
# and time

# chapter와 stage와 관련된 메소드들
def chapter_start(chapter_id):
    result = []

    dt = datetime.datetime.now(timezone.utc)
  
    utc_time = dt.replace(tzinfo=timezone.utc)
    utc_timestamp = utc_time.timestamp()
  
    print(utc_timestamp)
    result['chapter_id'] = chapter_id
    result['created_at'] = utc_timestamp

    return result

def chapter_clear(chapter_id):
    result = []

    return result

def stage_start(chapter_id, stage_id):
    result = []

    return result

def stage_clear(chapter_id, stage_id):
    result = []

    return result
