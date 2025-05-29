from fastapi import FastAPI 

app = FastAPI()


@app.get("/encore/")
async def myfunc():
    return {"message" : "ㅋㅋㅋㅋ "}


#터미널 실행코드 uvicorn myapi:app --reload
