from app import app, db
# from app.models import User, Post
from app.data.data_models import User, Post, Comment, UserRelation, DataObject, DataList
from app import mongodb


@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'User': User,
        'Post': Post,
        'Comment': Comment,
        'UserRelation': UserRelation,
        'DataObject': DataObject,
        'DataList': DataList,
        'mongodb': mongodb
    }
