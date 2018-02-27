from flask import Flask, render_template, request, session, redirect, url_for
from models import db, User
from forms import SignUpForm, LoginForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/python-flask-sqlalchemy'
db.init_app(app)

app.secret_key = "development-key"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if 'email' in session:
        return redirect(url_for('home'))
    else:
        form = SignUpForm()
        if request.method == 'POST':
            if not form.validate():
                return render_template('signup.html', form=form)
            else:
                user = User(form.first_name.data, form.last_name.data, form.email.data, form.password.data)
                db.session.add(user)
                db.session.commit()
                session['email'] = user.email
                return redirect(url_for('home', ))
        else:
            return render_template('signup.html', form=form)


@app.route('/login', methods=['POST', 'GET'])
def login():
    if 'email' in session:
        return redirect(url_for('home'))
    else:
        form = LoginForm()
        if request.method == 'POST':
            if not form.validate():
                return render_template('login.html', form=form)
            else:
                email = form.email.data
                password = form.password.data
                user = User.query.filter_by(email=email).first()
                if user and user.check_password(password):
                    session['email'] = email
                    return redirect(url_for('home', ))
                else:
                    return redirect(url_for('login'))
        else:
            return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    session.pop('email', None)
    return redirect(url_for('index'))


@app.route('/home')
def home():
    if 'email' not in session:
        return redirect(url_for('login'))
    else:
        return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
