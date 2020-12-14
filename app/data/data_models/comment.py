from datetime import datetime
from pymongo.collection import ObjectId

from app.data.data_models import DataObject


class Comment(DataObject):
    def __init__(self, author_id, content, time_stamp=datetime.utcnow):
        super().__init__()
        self._author_id = author_id
        self._content = content
        self._time_stamp = time_stamp() if callable(time_stamp) else time_stamp
        self._likes = self._dislikes = 0
        self._liked_by = []
        self._disliked_by = []
        self._is_deleted = False

    def __repr__(self):
        return f"Comment(id={self._id},author_id={self._author_id},content={self._content})"
