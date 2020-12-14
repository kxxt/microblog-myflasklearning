from pymongo import collection


class BaseQuery:
    def __init__(self, data_source: collection):
        self.src = data_source

    def __getattr__(self, name):
        return self.src.__getattribute__(name)

    def all(self):
        return self.src.find()

    def first_or_404(self):
        pass
