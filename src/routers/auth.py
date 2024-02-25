from fastapi import APIRouter, HTTPException, Depends, Response
from fastapi_login import LoginManager
from database.models import User
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_login.exceptions import InvalidCredentialsException
from fastapi.responses import JSONResponse
from utils.schema import UserCreated

router = APIRouter(prefix="/api/auth", tags=["Auth"])


SECRET = "e93e79597d15806e2e2a7baac7c6a6ac955732dbdd0d0fb0"
manager = LoginManager(SECRET, "/api/auth/login", use_cookie=True)


@manager.user_loader()
def query_user(username: str):
    """
    Get a user from the db
    :param user_id: E-Mail of the user
    :return: None or the user object
    """
    try:
        return User.get(username=username)
    except:
        pass


@router.get("/me")
async def me(user=Depends(manager)):
    user = user.__data__
    del user["password"]
    return user


@router.post("/login")
def login(data: OAuth2PasswordRequestForm = Depends()):
    username = data.username
    password = data.password
    content = {"message": "success."}
    response = JSONResponse(content=content)
    user = query_user(username)
    if not user:
        # you can return any response or error of your choice
        raise InvalidCredentialsException
    elif password != user.password:
        raise InvalidCredentialsException
    token = manager.create_access_token(data=dict(sub=user.username))
    manager.set_cookie(response, token)
    return response


@router.post("/register")
def register(data: UserCreated):
    try:
        user = User.create(**dict(data))
        return user.__data__
    except Exception as e:
        return f"error {e}"
