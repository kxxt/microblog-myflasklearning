from datetime import datetime
from pymongo.collection import ObjectId


class Post:
    def __init__(self, title, body, author=None, author_id=None, time_stamp=datetime.utcnow):
        self._id = ObjectId()
        self._title = title
        self._body = body
        if author and author_id:
            raise ValueError("You can only specify one of the following parameter: author,author_id")
        self._author_id = author.id or author_id
        self._likes = self.dislikes = 0
        self._liked_by = []
        self._disliked_by = []
        self._comments = []
        self._is_deleted = False
        self._time_stamp_init = time_stamp() if callable(time_stamp) else time_stamp
        self._time_stamp_final = self._time_stamp_init

    def __repr__(self):
        return f"Post(id={self._id},title={self._title},time={self._time_stamp_final})"