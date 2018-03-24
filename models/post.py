from datetime import datetime
from .database import Model

class Post(Model, table="pages"):
    @classmethod
    def new(cls, title, content):
        return super(Post, cls).new(
            title=title.title(),
            content=content,
            date=datetime.now().date()
        )
