'''from fastapi import FastAPI , Request

from pymongo import MongoClient

app = FastAPI()



conn= MongoClient("mongodb+srv://pranjaliathavale826_db_user:7R74U09HwACe19CX@cluster0.i9mbprw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")








@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}
    '''