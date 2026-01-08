from fastapi import FastAPI

app = FastAPI()
items = []


@app.get("/")
def root():
    return {"박성호": "시발련"}

@app.post("/items")
def create_item(item: str):
    items.append(item)
    return {
        "message": "아이템 추가 완료",
        "items": items
    }


