from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

'''
from fastapi import FastAPI , Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

conn= MongoClient("mongodb+srv://pranjaliathavale826_db_user:7R74U09HwACe19CX@cluster0.i9mbprw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    #database_link_var.database.collection (syntax)
    docs= conn.Notes.Notes.find({})
    newDocs= []
    for doc in docs:
            newDocs.append({
                 "id": doc["_id"],
                 "note": doc["note"]
            })
            print(newDocs)

    return templates.TemplateResponse(
        request=request, 
        name="index.html", 
        context= {"newDocs": newDocs}
    )





@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}
'''