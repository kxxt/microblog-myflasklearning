import unittest
from pymongo import MongoClient
from bson import ObjectId
import sys
# from ..base.data_object import DataObject
from ..base.data_list import DataList


class DataListCase(unittest.TestCase):
    def setUp(self):
        self.mongodb = MongoClient('localhost')
        self.dbs = self.mongodb.db
        self.test = self.dbs.test
        self.test.delete_many({})

    def tearDown(self):
        self.test.delete_many({})

    def generate(self):
        a_id = ObjectId()
        a = {
            '_id': a_id,
            'li': DataList(a_id, self.test, 'li')
        }
        return a, {'_id': a_id}

    def test___iadd__(self):
        a, cond = self.generate()
        self.test.insert_one(a)
        a['li'] += [1, 3, 4, 6]
        print(a)
        print(self.test.find_one(cond))
        assert a['li']
        assert a == self.test.find_one(cond)
        a['li'] += [23, 34, 54]
        print(a)
        print(self.test.find_one(cond))
        assert a['li']
        assert a['li'] == self.test.find_one(cond)['li']

    def test_extend(self):
        a, cond = self.generate()
        self.test.insert_one(a)
        a['li'].extend([1, 3, 4, 6])
        print(a)
        print(self.test.find_one(cond))
        assert a['li']
        assert a == self.test.find_one(cond)
        a['li'].extend([23, 34, 54])
        print(a)
        print(self.test.find_one(cond))
        assert a['li']
        assert a['li'] == self.test.find_one(cond)['li']
