from app import app, db
# from app.models import User, Post
from app.data.data_models import User, Post
from app import mongodb


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post, 'mongodb': mongodb}
