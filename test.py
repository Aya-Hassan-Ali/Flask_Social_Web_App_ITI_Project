# RUN THIS FILE WITH python test.py read_users
from mypackage import db,app
import sys
from mypackage.model import User, Post

# create database
def create_db():
	with app.app_context():
		# you will have instance folder with site.db inside
		db.create_all()

# -------------------------- CRUD OPERATIONS --------------------------
# Create operation
def create_user():
	with app.app_context():
		user = User(name='aya hassan',age='11',username='ayahassan33', email='ayahassan33@gmail.com', password='123')
		db.session.add(user)
		db.session.commit()
  
# Read operation
def read_user():
    with app.app_context():
        print(User.query.all())
        
# Update operation
def update_user():
	with app.app_context():
		user = User.query.filter_by(username="ayahassan33").first()
		user.username = 'ayahassan33'
		db.session.commit()
  		# print(user)
    
# Delete operation
def delete_user():
    with app.app_context():
        user = User.query.filter_by(username='ayahassan33').first()
        db.session.delete(user)
        db.session.commit()
        
             
# Create operation
def create_subject():
	with app.app_context():
		user = User.query.first()
		user1 = Post(id=1, name='Python', content='Python',duration=54, user_id=user.id)
		user2 = Post(id=2, name='php', content='php', duration=20,user_id=user.id)
		db.session.add(user1)
		db.session.add(user2)
		db.session.commit()

# Read operation
def read_user_subject():
    with app.app_context():
        user = User.query.first()
        print(user.posts)
        
# Read operation       
def read_post():
    with app.app_context():
        post = Post.query.first()
        print(post)
        print(post.user_id)
        
        
# snippet to allow us to run funcs from terminal with "python test.py print_func"
if __name__ == '__main__':
	globals()[sys.argv[1]]()