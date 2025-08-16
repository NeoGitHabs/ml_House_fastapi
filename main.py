from fastapi import FastAPI
import uvicorn
from api import property, review, auth, social_auth
from admin.setup import setup_admin
from starlette.middleware.sessions import SessionMiddleware
from config import SECRET_KEY


udemy = FastAPI()
udemy.include_router(property.property_router)
udemy.include_router(review.review_router)
udemy.include_router(auth.auth_router)
udemy.include_router(social_auth.social_router)
udemy.add_middleware(SessionMiddleware, secret_key=SECRET_KEY)
setup_admin(udemy)


if __name__ == '__main__':
    uvicorn.run(udemy, host='127.0.0.1', port=8001)
