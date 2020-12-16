from datetime import datetime
from pymongo.collection import ObjectId

from .base import DataObject, db_property, DataList
import app
from ..query import BaseQuery


class Comment(DataObject):
    def __init__(self, author_id, content, time_stamp=datetime.utcnow):
        super().__init__()
        self._author_id = author_id
        self._content = content
        self._time_stamp = time_stamp() if callable(time_stamp) else time_stamp
        self._likes = self._dislikes = 0
        self._liked_by = DataList(self._id, self.query.src, '_liked_by')
        self._disliked_by = DataList(self._id, self.query.src, '_disliked_by')
        self._is_deleted = False

    query = BaseQuery(app.mongodb.comments, dict())

    author_id = db_property('_author_id')
    content = db_property('_content')
    time_stamp = db_property('_time_stamp')
    likes = db_property('_likes')
    dislikes = db_property('_dislikes')
    is_deleted = db_property('_is_deleted')

    liked_by = db_property('_liked_by')
    disliked_by = db_property('_disliked_by')

    def __repr__(self):
        return f"Comment(id={self._id},author_id={self._author_id},content={self._content})"
