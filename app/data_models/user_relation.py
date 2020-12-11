from datetime import datetime
from enum import Enum


class RelationTypes(Enum):
    follow = 0
    blacklist = 1


class UserRelation:
    def __init__(self, from_id, to_id, reltype, time_stamp=datetime.utcnow):
        self._from_id = from_id
        self._to_id = to_id
        self._reltype = reltype
        self._time_stamp = time_stamp() if callable(time_stamp) else time_stamp
        self._is_deleted = False

    def __repr__(self):
        return f"UserRelation({self._from_id} {self._reltype.name} {self._to_id})"

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
