import uvicorn
from fastapi import FastAPI

from models import models
from database.database import engine
from routers import blog, user

app = FastAPI()
models.Base.metadata.create_all(engine)
app.include_router(blog.router)
app.include_router(user.router)


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
