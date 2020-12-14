from bson import ObjectId
import abc


class DataObject:
    def __init__(self):
        self._id = ObjectId()

    def to_dict(self):
        ret = dict()
        for k in self.__dict__.keys():
            if k[0] == '_' and k[1] != '_' and not callable(self.__dict__[k]):
                ret[k] = self.__dict__[k]
        return ret

    def full_save(self):
        cond = {'_id': self._id}
        old = self.query.find_one(cond)
        if old:
            self.query.update_one(cond, self.to_dict())
        else:
            self.query.insert_one(self.to_dict())
