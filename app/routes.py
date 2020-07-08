from flask import render_template
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Niraj'}
    posts = [
            {
                    'author': {'username': 'John'},
                    'body': 'Infor ION API'
            },
            {
                    'author': {'username': 'Susan'},
                    'body': 'Infor IDM'
            }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)