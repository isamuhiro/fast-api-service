from pydantic import BaseModel


class BlogSchema(BaseModel):
    title: str
    body: str

    class Config:
        orm_mode = True


class BlogRequest(BlogSchema):
    pass


class BlogCreate(BlogSchema):
    pass


class BlogResponse(BlogSchema):
    pass
