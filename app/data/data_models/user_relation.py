from datetime import datetime
from enum import Enum
import app

from .base import DataObject, db_property
from ..query import BaseQuery


class RelationTypes(Enum):
    follow = 0
    blacklist = 1


class UserRelation(DataObject):
    def __init__(self, from_id, to_id, reltype, time_stamp=datetime.utcnow):
        super().__init__()
        self._from_id = from_id
        self._to_id = to_id
        self._reltype = reltype
        self._time_stamp = time_stamp() if callable(time_stamp) else time_stamp
        self._is_deleted = False

    def __repr__(self):
        return f"UserRelation({self._from_id} {self._reltype.name} {self._to_id})"

    query = BaseQuery(app.mongodb.urels, dict())

    from_id = db_property('_from_id')
    to_id = db_property('_to_id')
    reltype = db_property('_reltype')
    time_stamp = db_property('_time_stamp')
    is_deleted = db_property('_is_deleted')

    @staticmethod
    def follow(from_u, to_u):
        pass

    @staticmethod
    def unfollow(from_u, to_u):
        pass

    @staticmethod
    def blacklist(from_u, to_u):
        pass

    @staticmethod
    def unblacklist(from_u, to_u):
        pass
