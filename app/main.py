from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {"message": "FastAPI 项目启动成功"}