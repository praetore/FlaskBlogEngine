from app import db
from app.models import Post

__author__ = 'darryl'


def create_post(form):
    author = form.author.data
    content = form.content.data
    post = Post(content=content, author=author)
    db.session.add(post)
    db.session.commit()