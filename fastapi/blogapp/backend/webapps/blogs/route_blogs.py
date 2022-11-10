from fastapi import APIRouter, Request, Depends, responses, status
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from fastapi.security.utils import get_authorization_scheme_param

from db.repository.blogs import retrieve_blog, list_blogs, create_new_blog
from db.session import get_db
from webapps.blogs.forms import BlogCreationForm
from schemas.blogs import BlogCreate
from apis.v1.route_login import get_current_user_from_token
from db.models.users import User

templates = Jinja2Templates(directory="templates")
router = APIRouter(include_in_schema=False)

@router.get("/")
async def home(request: Request, db: Session = Depends(get_db), msg: str = None):
    blogs = list_blogs(db=db)
    return templates.TemplateResponse(
        "general_pages/homepage.html", {"request":request, "blogs": blogs, "msg": msg}
    )

@router.get("/details/{id}")
def blog_detail(id: int, request: Request, db:Session = Depends(get_db)):
    blog = retrieve_blog(id=id, db=db)
    return templates.TemplateResponse(
        "blogs/detail.html", {"request": request, "blog": blog}
    )

@router.get("/post-a-blog/")
def create_blog(request: Request, db: Session = Depends(get_db)):
    return templates.TemplateResponse("blogs/create_blog.html", {"request": request})

@router.post("/post-a-blog/")
async def create_blog(request: Request, 
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user_from_token)):
    form = BlogCreationForm(request)
    await form.load_data()
    if form.is_valid():
        try:
            token = request.cookies.get("access_token")
            scheme, param = get_authorization_scheme_param(
                token
            )  # scheme will hold "Bearer" and param will hold actual token value
            current_user: User = get_current_user_from_token(token=param, db=db)
            blog = BlogCreate(**form.__dict__)
            blog = create_new_blog(blog=blog, db=db, owner_id=current_user.id)
            return responses.RedirectResponse(
                f"/details/{blog.id}", status_code=status.HTTP_302_FOUND
            )
        except Exception as e:
            print(e)
            form.__dict__.get("errors").append(
                "You might not be logged in, In case problem persists please contact us."
            )
            return templates.TemplateResponse("blogs/create_blog.html", form.__dict__)
    return templates.TemplateResponse("blogs/create_blog.html", form.__dict__)

@router.get("/delete-blog/")
def show_blogs_to_delete(request: Request, db: Session = Depends(get_db)):
    blogs = list_blogs(db=db)
    return templates.TemplateResponse(
        "blogs/show_blogs_to_delete.html", {"request": request, "blogs": blogs}
    )