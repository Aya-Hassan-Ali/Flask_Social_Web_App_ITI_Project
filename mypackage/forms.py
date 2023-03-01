from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, IntegerField, HiddenField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from mypackage.model import User, Post

class RegistrationForm(FlaskForm):
	username = StringField(
		'Username',
		validators=[
			DataRequired(),
			Length(min=3, max=20)
		]
	)
	email = StringField(
		'Email',
		validators=[
			DataRequired(),
			Email()
		]
	)
	password = PasswordField(
		'Password',
		validators=[
			DataRequired()
		]
	)
	confirm_password = PasswordField(
		'Confirm Password',
		validators=[
			DataRequired(),
			EqualTo('password')
		]
	)
	name = StringField(
		'Name',
		validators=[
			DataRequired(),
			Length(min=3, max=20)
		]
	)
	age = IntegerField(
			'Age',
			validators=[
				DataRequired()
			]
		)
	submit = SubmitField(
		'Sign Up'
	)


	# custom validation for duplicates
	def validate_username(self, username):
		user = User.query.filter_by(username=username.data).first()
		if user:
			raise ValidationError('Username already exists')

	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError('Email already exists')


class LoginForm(FlaskForm):
	username  = StringField(
		'Username',
		validators=[
			DataRequired(),
			Length(min=3, max=20)
		]
	)
	password = PasswordField(
		'Password',
		validators=[
			DataRequired()
		]
	)
	submit = SubmitField(
		'Sign In'
	)
 
 
class PostForm(FlaskForm):
    
    content = TextAreaField(
        'Content',
        validators=[
                    DataRequired(),
                   ]
    )
    # duration = IntegerField(
    #     'Duration',
    #     validators=[
    #                 DataRequired(),
    #                ]
    # )
    user_id = IntegerField(
		'user ID',
        validators=[
                    DataRequired()
                   ],
        # render_kw={'readonly':True}
	)
    submit = SubmitField(
        'Submit',
    ) 