from bson import ObjectId
from functools import partialmethod


class DataObject:
    def raw_update(self, field, value, method='$set'):
        self.__getattribute__('query').update_one(self.__cond
                                                  ,
                                                  {
                                                      method: {
                                                          field: value
                                                      }
                                                  })

    def update_field(self, field, method='$set'):
        self.raw_update(field, self.__getattribute__(field), method)

    def increase_field(self, field, delta):
        # NOTICE:
        self.__dict__[field] += delta
        self.raw_update(self.__cond, field, method='$inc')

    # def update_array_field(self, array_name):

    def __init__(self):
        self._id = ObjectId()
        self.__cond = {'_id': self._id}

    def to_dict(self):
        ret = dict()
        for k in self.__dict__.keys():
            if k[0] == '_' and k[1] != '_' and not callable(self.__dict__[k]):
                ret[k] = self.__dict__[k]
        return ret

    def full_save(self):
        cond = {'_id': self._id}
        old = self.__getattribute__('query').find_one(cond)
        if old:
            self.__getattribute__('query').update_one(cond, self.to_dict())
        else:
            self.__getattribute__('query').insert_one(self.to_dict())
