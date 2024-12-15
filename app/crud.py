from sqlalchemy.orm import Session
from .models import User, Post
from .schemas import UserCreate, PostCreate

def create_user(db: Session, user: UserCreate):
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_users(db: Session):
    return db.query(User).all()

def create_post(db: Session, post: PostCreate):
    db_post = Post(**post.dict())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def get_posts(db: Session):
    return db.query(Post).all()

def get_posts_by_user(db: Session, user_id: int):
    return db.query(Post).filter(Post.user_id == user_id).all()