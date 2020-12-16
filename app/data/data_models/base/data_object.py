from bson import ObjectId
from .data_list import DataList


def db_property(field_name):
    def getter(self):
        return self.__dict__[field_name]

    def setter(self, value):
        self.__dict__[field_name] = value
        self.update_field(field_name)

    return property(getter, setter)


class DataObject:
    """警告: 开发尚不完善!
    如果两个DataObject 指向同一个数据库文档 , 其中一个DataObject做的更改不会反映在另一个中!!!
    如果多个Object都对数据库进行了操作, 此时状态会极其不一致!!!"""
    query = None

    def raw_update(self, field, value, method='$set'):
        self.query.update_one(self.__cond
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

    id = db_property('_id')

    def to_dict(self):
        ret = dict()
        for k in self.__dict__.keys():
            if k[0] == '_' and k[1] != '_' and k[2:].find('__') == -1 and not callable(self.__dict__[k]):
                ret[k] = self.__dict__[k]
        return ret

    @classmethod
    def from_dict(cls, dic, col, pre='', root_id=None):
        ret = cls.__new__(cls)
        if not root_id:
            root_id = dic['_id']
        for key in dic:
            if isinstance(dic[key], list):
                ret.__dict__[key] = DataList.from_list(root_id, col, pre + '.' + key, dic[key])
            elif isinstance(dic[key], dict):
                raise NotImplementedError()
            else:
                ret.__dict__[key] = dic[key]
        return ret

    def full_save(self):
        cond = {'_id': self._id}
        old = self.query.find_one(cond)
        if old:
            self.query.update_one(cond, self.to_dict())
        else:
            self.query.insert_one(self.to_dict())
