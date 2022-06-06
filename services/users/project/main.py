import sys    
print("In module products sys.path[0], __package__ ==", sys.path[0], __package__)
from fastapi import Depends, FastAPI, Body
from project.api.users import router as user_router

app = FastAPI()
app.include_router(user_router)
