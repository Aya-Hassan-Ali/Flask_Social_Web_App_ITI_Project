from mypackage import * 
from flask import render_template, url_for, redirect, flash, Blueprint, session
from mypackage.forms import RegistrationForm, LoginForm, PostForm
from mypackage.model import User, Post
from flask import request
from test import create_db
from flask_login import login_user, current_user, logout_user, login_required
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt()

# blueprint
users = Blueprint(
	'users',
	__name__,
	url_prefix='/users'
)

menue={
        'Home': "/home",
        'About': "/about",
        'Registration': "/users/register",
        'Login': "/users/login",
        'Posts': "/post/add",
        'Logout':"/logout",
        
    }


# home routing
@app.route('/')


@app.route('/home')
def home():
    create_db()   
    return render_template('home.html',title="Home Page", menue=menue)


# about routing
@app.route('/about')
@login_required
def about():
	return render_template('about.html', title ="About page", menue=menue)

# redirect function
@app.route('/redirect')
def redirectFun():
    return redirect(url_for('home'))


@users.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Registration Successful. You can now log in. {form.username.data} , {form.password.data}", "success"')
        with app.app_context():
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf8')
            new_user=User(name=form.name.data, age=form.age.data, username=form.username.data, email=form.email.data, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
        flash(f"Registration Successful {form.username.data}", "success")
        return redirect(url_for('users.login'))
            
    return render_template('register.html', title='Registration Page', form=form, menue=menue)


@users.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()

    if form.validate_on_submit():        
        user = User.query.filter_by(username=form.username.data).first()
        # if user exists , check his password
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user)
            flash(f"Login Successful {user.username}", "success")
            return redirect(url_for('home'))
        else:
            flash(f"Incorrect username or password. Please try again.", "danger")
            return render_template('login.html', title='Login Page', form=form, menue=menue)
        
    return render_template('login.html', title='Login Page', form=form, menue=menue)
        

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('home'))


# @app.route('/profile')
# def index():
#     students = User.query.all()
#     return render_template('Profile.html', title='Profile',users=users,menue=menue)

@app.route('/post/add', methods=['GET', 'POST'])
def post_add():
    form = PostForm()
    if form.validate_on_submit():
        # session['user_id'] = user.id
        # current_user = user.query.filter_by(id=session['id']).first()
        post = Post(name=form.name.data, content=form.content.data, duration=form.duration.data, user_id=form.user_id.data)
        db.session.add(post)
        db.session.commit()
        flash('Post added successfully!')
        return redirect(url_for('home'))
    
    return render_template('postAdd.html', form=form, menue=menue, title="Add Post Page")
