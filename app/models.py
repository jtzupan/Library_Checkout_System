import datetime
from app import db, login
from flask_login import UserMixin
from hashlib import md5
from werkzeug.security import generate_password_hash, check_password_hash


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    common_id = db.Column(db.Integer, index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(digest, size)


class Book(db.Model):
    current_time = datetime.datetime.utcnow()
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), unique=True)
    author = db.Column(db.String(128))
    published_year = db.Column(db.Integer)
    added_date = db.Column(db.DateTime, default=current_time)
    description_id = db.relationship('BookDescriptionDim', backref='book', lazy='dynamic')

    def __repr__(self):
        return '<Title {}>'.format(self.title)


class DescriptionDim(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(128))

    def __repr__(self):
        return '<Description {}>'.format(self.description)


class BookDescriptionDim(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    description_id = db.Column(db.Integer, db.ForeignKey('description_dim.id'))

    def __repr__(self):
        return '<Book ID {}>'.format(self.description_id)


class CheckoutTransfact(db.Model):
    current_time = datetime.datetime.utcnow()
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    checkout_date = db.Column(db.DateTime, default=current_time)
    due_date = db.Column(db.DateTime, default=current_time + datetime.timedelta(14))
    checkin_date = db.Column(db.DateTime)

    def __repr__(self):
        return '<Checkout ID {}>'.format(self.id)