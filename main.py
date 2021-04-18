import uvicorn
from fastapi import FastAPI

from models import models
from database.database import engine
from routers import blog


app = FastAPI()
models.Base.metadata.create_all(engine)
app.include_router(blog.router)


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
