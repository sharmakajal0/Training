from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status
from typing import List

from db.session import get_db
from db.models.blogs import Blog
from db.models.users import User
from schemas.blogs import BlogCreate, ShowBlog
from db.repository.blogs import create_new_blog, retrieve_blog, list_blogs, update_blog_by_id, delete_blog_by_id
from apis.v1.route_login import get_current_user_from_token

router = APIRouter()

@router.post("/create-blog/", response_model=ShowBlog)
def create_blog(blog: BlogCreate, db: Session = Depends(get_db), current_user:User = Depends(get_current_user_from_token)):
    blog = create_new_blog(blog=blog, db=db, owner_id=current_user)
    return blog


@router.get("/get/{id}", response_model=ShowBlog)
def read_blog(id:int, db:Session = Depends(get_db)):
    blog = retrieve_blog(id=id, db=db)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with this id {id} does not exist")
    
    return blog

@router.get("/all", response_model=List[ShowBlog])
def read_blogs(db:Session = Depends(get_db)):
    blogs = list_blogs(db=db)
    return blogs

@router.put("/update/{id}")
def update_blog(id: int, blog: BlogCreate, db: Session = Depends(get_db)):
    current_user = 1
    message = update_blog_by_id(id=id,blog=blog,db=db, owner_id=current_user)
    if not message:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id {id} not found")
    
    return {"msg": "Successfully Updated Blog."}

@router.delete("/delete/{id}")
def delete_blog(id: int, db:Session = Depends(get_db), current_user: User = Depends(get_current_user_from_token)):
    blog = retrieve_blog(id=id, db=db)
    if not blog:
        return HTTPException()
    print(blog.owner_id,current_user.id)
    if blog.owner.id == current_user.id:
        delete_blog_by_id(id=id, db=db, owner_id=current_user)
        return {"detail": "Successfully Deleted"}
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"You are not permitted to delete the blog!!")
    
    