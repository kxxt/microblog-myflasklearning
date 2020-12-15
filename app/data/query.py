from pymongo import collection


class BaseQuery:
    def __init__(self, data_source: collection, custom_query: dict):
        self.src = data_source
        self.custom_query = custom_query

    def __getattr__(self, name):
        if name in self.custom_query:
            return self.custom_query[name]
        else:
            return self.src.__getattribute__(name)

    def all(self):
        return self.src.find()

    def first_or_404(self):
        pass
