from pymongo import MongoClient

users = None
posts = None
rels = None
comments = None


class DBHandler:
    def __init__(self, papp):
        self.client = MongoClient(papp.config.get('MONGODB_HOST'), papp.config.get('MONGODB_PORT'))
        self.users = self.client.users
        self.posts = self.client.posts
        self.urels = self.client.urels
        self.comments = self.client.comments
