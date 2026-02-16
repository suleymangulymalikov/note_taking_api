from fastapi import APIRouter, Query, HTTPException
from typing import Optional, List
from datetime import datetime

from app.models import Note, NoteCreate
from app.db import notes_db 

router = APIRouter()


@router.get("/notes", response_model=List[Note])
def get_all_notes(skip: int = Query(0, ge=0), limit: int = Query(10, ge=1, le=100), tag: Optional[str] = None, search: Optional[str] = None):
    filtered_notes = notes_db
    
    # Filter by Tag
    if tag is not None:
        tag_filtered = []

        for note in filtered_notes:
            if note.tags and tag in note.tags:
                tag_filtered.append(note)

        filtered_notes = tag_filtered 

    # Filter by search
    if search:
        search = search.strip().lower()
        if search:
            search_filtered = []
            for note in filtered_notes:
                if search in note.title.lower() or search in note.content.lower():
                    search_filtered.append(note)

            filtered_notes = search_filtered

        
    return filtered_notes[skip : skip + limit]

@router.post("/notes", status_code=201, response_model=Note)
def create_note(note: NoteCreate):
    new_id = 1 if not notes_db else max(note.id for note in notes_db) + 1
    created_at = datetime.now()
    updated_at = datetime.now()

    new_note = Note(
        title = note.title,
        content = note.content,
        tags = note.tags,
        id = new_id,
        created_at = created_at,
        updated_at = updated_at        
    )
    
    notes_db.append(new_note)

    return new_note


@router.get("/notes/{note_id}", response_model=Note, responses={ 404: { "detail": "Note not found" } })
def get_note_by_id(note_id: int):
    for note in notes_db:
        if note.id == note_id:
            return note 
    raise HTTPException(status_code=404, detail="Note not found")


@router.put("/notes/{note_id}", response_model=Note, responses={ 404: { "detail": "Note not found" } })
def update_note_by_id(note_id: int, note_update: NoteCreate):
    for note in notes_db:
        if note.id == note_id:
            note.title = note_update.title 
            note.content = note_update.content 
            note.tags = note_update.tags
            note.updated_at = datetime.now()
            return note
    
    raise HTTPException(status_code=404, detail="Note not found")

@router.delete("/notes/{note_id}", status_code=204, responses={ 404: { "detail": "Note not found" } })
def delete_note_by_id(note_id: int):
    for idx, note in enumerate(notes_db):
        if note.id == note_id:
            notes_db.pop(idx)
            return
    
    raise HTTPException(status_code=404, detail="Note not found")