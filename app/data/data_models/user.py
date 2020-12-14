from datetime import datetime
from hashlib import md5

from pymongo.collection import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

import app
from collections import MutableMapping

from app.data.data_models.data_object import DataObject
from app.data.query import BaseQuery


class User(DataObject):
    def __init__(self, username, passwd, email, query, friendly_name=None, about='', register_date=datetime.utcnow):
        super().__init__()
        self._username = username
        self._passwd_hash = generate_password_hash(passwd)
        if not email:
            raise ValueError('Email can\'t be empty!')
        self._email = email
        self._friendly_name = friendly_name or username
        self._about = about
        self._register_date = register_date() if callable(register_date) else register_date
        self._following_count = 0
        self._followers_count = 0
        self._is_deleted = False
        self._last_seen = self._register_date
        self._posts_cnt = 0
        self._is_from_db = False

    query = BaseQuery(app.mongodb.users)

    @property
    def id(self):
        return id

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        self._username = value
        self.query.update()
        # TODO:

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        pass

    @property
    def friendly_name(self):
        return self._friendly_name

    @friendly_name.setter
    def friendly_name(self, value):
        pass

    @property
    def about(self):
        return self._about

    @about.setter
    def about(self, value):
        pass

    def __repr__(self):
        return f"User(id={self._id},username={self._username},friendly_name={self._friendly_name},email={self._email})"

    def save(self):
        pass

    def check_password(self, password):
        return check_password_hash(self._passwd_hash, password)

    def avatar(self, size):
        digest = md5(self._email.lower().encode('utf-8')).hexdigest()
        return f'https://www.gravatar.com/avatar/{digest}?d=identicon&s={size}'

    def get_all_posts(self):
        pass

    def get_all_followers(self):
        pass

    def get_all_following(self):
        pass

    def unregister(self):
        pass

    def reset_password(self, passwd):
        pass


