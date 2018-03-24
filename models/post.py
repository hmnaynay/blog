from datetime import datetime
from .database import Document, db

class Post(Document):
    _collection = db.posts
    _schema = [
        'title',
        'content'
    ]
    _check = _schema

    @staticmethod
    def _format_new(**kwargs):
        return {
            **kwargs,
            'date': datetime.now().date()
        }
