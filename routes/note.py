#router mai pura logic jata hai

from fastapi import APIRouter
#router which helps to plug in with index.html
from models.note import Note
from config.db import conn
from schemas.note import noteEntity, notesEntity

from fastapi import FastAPI , Request
from fastapi.responses import HTMLResponse

from fastapi.templating import Jinja2Templates
from pymongo import MongoClient

note= APIRouter()

templates = Jinja2Templates(directory="templates")

@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs = conn.Notes.Notes.find({})
    newDocs = notesEntity(docs) # This uses your schema safely!

    return templates.TemplateResponse(
        request=request, 
        name="index.html", 
        context={"newDocs": newDocs}
    )

'''
@note.post("/")
def add_note(note: Note): #Note is coming from model (structure)
    print(note)
    inserted_note= conn.Notes.Notes.insert_one(dict(note))
    return notesEntity(inserted_note) #this coverts the model structure into scheme
'''

@note.post("/")
async def read_item(request: Request):
    form= await request.form()
    formDict= dict(form)
    formDict["important"]= True if formDict["important"]== "on" else False
         
    '''note= conn.Notes.Notes.insert_one(formDict)
    return {"Success": True}'''

    # 1. Save to database
    conn.Notes.Notes.insert_one(formDict)
    
    # 2. Fetch all notes (including the new one)
    docs = conn.Notes.Notes.find({})
    newDocs = notesEntity(docs)
    
    # 3. Render the template right here so the page updates instantly
    return templates.TemplateResponse(
        request=request, 
        name="index.html", 
        context={"newDocs": newDocs}
    )