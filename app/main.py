from fastapi import FastAPI
from .domain.gatcha import weighted_gatcha, rated_gatcha

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
