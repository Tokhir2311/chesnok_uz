from datetime import datetime

from sqlalchemy import Integer, String, BigInteger, Text, text, func
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base



class BaseModel(Base):
    __abstract__ = True 

    id:Mapped[int] = mapped_column(BigInteger, primary_key=True)
    created_at:Mapped[datetime] = mapped_column(Datetime(timezone=True), default = func.now())
    updated_at:Mapped[datetime] = mapped_column(Datetime(timezone=True), onupdate = func.now())


class Media(Base):
    __tablename__="media"

    pass

class PostMedia(Base):
    __tablename__="post_media"

    pass

class Post(BaseModel):
    __tablename__ = "post"

    


class Category(BaseModel):
    __tablename__="category"

    post_id:Mapped[int] = mapped_column(BigInteger, NULLABLE = True)
    name:Mapped[str] = mapped_column(String)


class Rating(BaseModel):
    __tablename__= "rating"

    count:Mapped[int] = mapped_column(BigInteger)

class Journalist(BaseModel):
    __tablename__="journalist"

    avatar:Mapped[str] = mapped_column(String)
    name:Mapped[str] = mapped_column(String, Nullable=True)
    surname:Mapped[str] = mapped_column(String)
    bio:Mapped[str] = mapped_column(Text)


