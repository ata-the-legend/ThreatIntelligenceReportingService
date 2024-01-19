from fastapi import FastAPI
from routers import users, reports

app = FastAPI()

app.include_router(users.router)
app.include_router(reports.router)