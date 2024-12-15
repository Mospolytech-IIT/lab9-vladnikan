from app import crud, database, models, schemas
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db, user)

@app.get("/users/", response_model=list[schemas.UserResponse])
def read_users(db: Session = Depends(get_db)):
    return crud.get_users(db)

@app.post("/posts/", response_model=schemas.PostResponse)
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.id == post.user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.create_post(db, post)

@app.get("/posts/", response_model=list[schemas.PostResponse])
def read_posts(db: Session = Depends(get_db)):
    return crud.get_posts(db)

@app.get("/posts/user/{user_id}", response_model=list[schemas.PostResponse])
def read_posts_by_user(user_id: int, db: Session = Depends(get_db)):
    return crud.get_posts_by_user(db, user_id)
