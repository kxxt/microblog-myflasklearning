class DataList(list):
    @staticmethod
    def from_list(container_id, container_collection, field_name, li):
        ret = DataList(container_id, container_collection, field_name)
        ret.extend(li)
        return ret

    def __init__(self, container_id, container_collection, field_name, *args, **kwargs):
        self.__col = container_collection
        self.__field_name = field_name
        self.__cond = {'_id': container_id}
        super().__init__(*args, **kwargs)

    def __iadd__(self, other):
        self.__col.update_one(self.__cond,
                              {
                                  '$push': {
                                      self.__field_name: {
                                          '$each': other
                                      }
                                  }
                              })
        return super().__iadd__(other)

    def extend(self, other):
        self.__iadd__(other)

    def __setitem__(self, key, value):
        self.__col.update_one(self.__cond,
                              {
                                  '$set': {
                                      f'{self.__field_name}.{key}': value
                                  }
                              })
        super().__setitem__(key, value)

    def __mul__(self, other):
        raise NotImplementedError('leftMul is not implemented because of safety concerns.')

    def __rmul__(self, other):
        raise NotImplementedError('rightMul is not implemented because of safety concerns.')

    def __imul__(self, other):
        raise NotImplementedError('iMul is not implemented because of safety concerns.')

    def append(self, item):
        self.__col.update_one(self.__cond,
                              {
                                  '$push': {
                                      self.__field_name: item
                                  }
                              })
        super().append(item)

    def clear(self):
        self.__col.update_one(self.__cond,
                              {
                                  '$set': {
                                      self.__field_name: []
                                  }
                              })
        super().clear()

    def insert(self, index, value):
        self.__col.update_one(self.__cond,
                              {
                                  '$push': {
                                      self.__field_name: {
                                          '$each': [value],
                                          '$position': index
                                      }
                                  }
                              })
        super().insert(index, value)

    def remove(self, one):
        """WARNING: The implementation of this remove differs from list.remove(). Because it's not efficient and easy
        to remove a single element in a list in mongodb , this `remove` method removes *all* elements that satisfy
        the condition. Workarounds exist but I won't adopt them. See more : https://jira.mongodb.org/browse/SERVER-1014"""
        self.__col.update_one(self.__cond, {
            '$pull': {
                self.__field_name: {
                    '$in': [one]
                }
            }
        })
        while one in self:
            super().remove(one)

    def pop(self, index=None):
        if index:
            self.__col.update_one(self.__cond, {
                '$pull': {
                    self.__field_name: {
                        '$position': index
                    }
                }
            })
            return super().pop(index)
        else:
            self.__col.update_one(self.__cond, {
                '$pop': {
                    self.__field_name: 1
                }
            })
            return super().pop()

    def sort(self, func=None, reverse=False):
        raise NotImplementedError("Sort is currently not implemented!")

    def reverse(self):
        raise NotImplementedError('Reverse is currently not implemented')
