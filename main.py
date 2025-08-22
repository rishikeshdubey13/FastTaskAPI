from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from config import settings
import os

app = FastAPI()

# Database configuration
DATABASE_URL = settings.database_url
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    completed = Column(Boolean, default= False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

# Create the database tables
Base.metadata.create_all(bind=engine)

# Pydantic model for request/response
class TaskCreate(BaseModel):
    title: str
    description: str
    completed: bool= False


class TaskResponse(TaskCreate):
    id:int
    created_at: datetime

    class Config:
        orm_mode = True


#database dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
    

@app.get("/")
def read_root():
    return {"Hello": "World"}