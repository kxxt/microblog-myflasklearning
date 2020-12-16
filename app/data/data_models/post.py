from datetime import datetime
from pymongo.collection import ObjectId
import app

from .base import DataObject, DataList, db_property
from ..query import BaseQuery


class Post(DataObject):
    def __init__(self, title, body, author=None, author_id=None, time_stamp=datetime.utcnow):
        super().__init__()
        self._title = title
        self._body = body
        if author and author_id:
            raise ValueError("You can only specify one of the following parameter: author,author_id")
        self._author_id = author.id or author_id
        self._likes = self._dislikes = 0
        self._liked_by = DataList(self._id, self.query.src, '_liked_by')
        self._disliked_by = DataList(self._id, self.query.src, '_disliked_by')
        self._comments = DataList(self._id, self.query.src, '_comments')
        self._is_deleted = False
        self._time_stamp_init = time_stamp() if callable(time_stamp) else time_stamp
        self._time_stamp_final = self._time_stamp_init

    query = BaseQuery(app.mongodb.posts, dict())

    title = db_property('_title')
    body = db_property('_body')
    author_id = db_property('_author_id')
    likes = db_property('_likes')
    dislikes = db_property('_dislikes')
    is_deleted = db_property('_is_deleted')
    time_stamp_init = db_property('_time_stamp_init')
    time_stamp_final = db_property('_time_stamp_final')

    def __repr__(self):
        return f"Post(id={self._id},title={self._title},time={self._time_stamp_final})"
