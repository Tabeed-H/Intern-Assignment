from fastapi import  APIRouter                      # Import fastapi router
from app.api.handlers import user                   # Import User Routes
from app.api.auth.jwt import authRouter             # Import User Authenticated Routes

router = APIRouter()        # Create instance of Router

router.include_router(user.userRouter, prefix='/users', tags=['users'])     # User Routes
router.include_router(authRouter, prefix='/auth', tags=['auth'])            # User Routes that require authentication
