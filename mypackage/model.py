# pip install flask-sqlalchemy
from mypackage import db, login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    age = db.Column(db.Integer)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    profile_image = db.Column(db.String(120))
    posts = db.relationship('Post', backref='editor', lazy=True)
    
def __repr__(self):
		return f"User('{self.username}', '{self.password}')"


    
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    content = db.Column(db.Text)
    # duration = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    
def __repr__(self):
		return f"Post('{self.name}', '{self.duration}')"
    