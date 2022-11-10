from sqlalchemy.orm import Session

from schemas.blogs import BlogCreate
from db.models.blogs import Blog

def create_new_blog(blog: BlogCreate, db: Session, owner_id: int):
    blog_object = Blog(**blog.dict(), owner_id=owner_id)
    db.add(blog_object)
    db.commit()
    db.refresh(blog_object)
    return blog_object

def retrieve_blog(id:int, db:Session):
    blog = db.query(Blog).filter(Blog.id == id).first()
    return blog

def list_blogs(db: Session):
    blogs = db.query(Blog).all()
    return blogs

def update_blog_by_id(id: int, blog:BlogCreate, db:Session, owner_id):
    existing_blog = db.query(Blog).filter(Blog.id==id)
    if not existing_blog.first():
        return 0
    blog.__dict__.update(owner_id=owner_id)
    existing_blog.update(blog.__dict__)
    db.commit()
    return 1

def delete_blog_by_id(id: int, db: Session, owner_id):
    existing_blog = db.query(Blog).filter(Blog.id==id)
    if not existing_blog.first():
        return 0
    existing_blog.delete(synchronize_session=False)
    db.commit()
    return 1