from fastapi import FastAPI

app = FastAPI()
items = []


@app.get("/")
def root():
    return {"박성호": "시발련"}


