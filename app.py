# from flask import Flask, request

# # Create a Flask app instance
# app = Flask(__name__)

# # Define a route and a view function
# @app.route('/')
# def hello_world():
#     return 'Hello, World!'

# if __name__ == '__main__':
#     # Run the Flask app
#     app.run()














# from flask import Flask, request

# # Create a Flask app instance
# app = Flask(__name__)
# @app.route('/')
# def home():
#     return 'Welcome to the Home Page'

# @app.route('/about')
# def about():
#     return 'This is the About Page'














# from flask import Flask, request

# # Create a Flask app instance
# app = Flask(__name__)
# @app.route('/user/<username>')
# def show_user_profile(username):
#     return f'User: {username}'



















# from flask import Flask, request

# # Create a Flask app instance
# app = Flask(__name__)
# @app.route('/submit', methods=['GET','POST'])
# def submit_form():
#     if request.method == 'POST':
#         # Process form data
#         return 'Form submitted successfully'
#     return 'Submit your form here'



















# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html', title='Home', content='Welcome to my website')

# if __name__ == '__main__':
#     app.run()





















# from flask import Flask, request, make_response

# app = Flask(__name__)

# @app.route('/cookie')
# def set_cookie():
#     resp = make_response('Cookie set!')
#     resp.set_cookie('my_cookie', 'cookie_value')
#     return resp

# @app.route('/get_cookie')
# def get_cookie():
#     cookie_value = request.cookies.get('my_cookie')
#     return f'Cookie value: {cookie_value}'

# if __name__ == '__main__':
#     app.run()




























# from flask import Flask, request, render_template, redirect, session, url_for

# app = Flask(__name__)

# # Set a secret key for session management (replace 'your_secret_key' with a secret key of your choice)
# app.secret_key = 'your_secret_key'

# # Example of a route that sets session data
# @app.route('/set_session/<value>')
# def set_session(value):
#     session['data'] = value
#     return 'Session data set successfully.'

# # Example of a route that retrieves session data
# @app.route('/get_session')
# def get_session():
#     data = session.get('data')
#     if data is not None:
#         return f'Session data: {data}'
#     else:
#         return 'Session data is not set.'

# # Example of a route that clears session data
# @app.route('/clear_session')
# def clear_session():
#     session.pop('data', None)
#     return 'Session data cleared.'

# # Example of a simple login route using session
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']

#         # Replace this with your actual authentication logic
#         if username == 'user' and password == 'password':
#             session['logged_in'] = True
#             return redirect(url_for('dashboard'))
#         else:
#             return 'Login failed. Please try again.'

#     return render_template('login.html')

# # Example of a protected route that requires login
# @app.route('/dashboard')
# def dashboard():
#     if session.get('logged_in'):
#         return 'Welcome to the dashboard!'
#     else:
#         return redirect(url_for('login'))

# if __name__ == '__main__':
#     app.run(debug=True)























# from flask import Flask, request

# # Create a Flask app instance
# app = Flask(__name__)

# @app.errorhandler(404)
# def not_found_error(error):
#     return '404 Not Found', 500





















# from flask import Flask
# from flask_login import LoginManager, UserMixin

# app = Flask(__name__)
# login_manager = LoginManager(app)

# class User(UserMixin):
#     pass

# @login_manager.user_loader
# def load_user(user_id):
#     return User.get(user_id)

# @app.route('/login')
# def login():
#     # Your login logic here
#     return 'User logged in successfully'

# @app.route('/logout')
# def logout():
#     # Your logout logic here
#     return 'User logged out successfully'





















# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)

# @app.route('/create_user/<username>')
# def create_user(username):
#     user = User(username=username)
#     db.session.add(user)
#     db.session.commit()
#     return f'User {username} created successfully'

























# from flask import Flask
# from flask_restful import Resource, Api

# app = Flask(__name__)
# api = Api(app)

# class HelloWorld(Resource):
#     def get(self):
#         return {'message': 'Hello, World!'}

# api.add_resource(HelloWorld, '/')

# if __name__ == '__main__':
#     app.run(debug=True)






















# from flask import Flask, render_template
# from flask_wtf import FlaskForm
# from wtforms import StringField, SubmitField
# from wtforms.validators import DataRequired

# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'your_secret_key'

# class MyForm(FlaskForm):
#     name = StringField('Name', validators=[DataRequired()])
#     submit = SubmitField('Submit')

# @app.route('/form', methods=['GET', 'POST'])
# def form():
#     form = MyForm()
#     if form.validate_on_submit():
#         return f'Hello, {form.name.data}!'
#     return render_template('form.html', form=form)





















# from flask import Flask
# from flask_mail import Mail, Message

# app = Flask(__name__)
# app.config['MAIL_SERVER'] = ''
# app.config['MAIL_PORT'] = 587
# app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USERNAME'] = ''
# app.config['MAIL_PASSWORD'] = ''

# mail = Mail(app)

# @app.route('/send_email')
# def send_email():
#     msg = Message('Hello', sender='m.m.shahmeh@gmail.com', recipients=['m.m.shahmeh@gmail.com'])
#     msg.body = 'This is a test email.'
#     mail.send(msg)
#     return 'Email sent successfully'
