from fastapi import FastAPI
from routers import users, reports,authentications

import os

app = FastAPI()

app.include_router(authentications.router)
app.include_router(users.router)
app.include_router(reports.router)

# JWT
SECRET_KEY = os.environ.get("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
"09d25e094faa6ca2556c818166b7hso3b93f7099f6f0f4caa6cf63b88e8d3e9"