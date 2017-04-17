from app import db, bcrypt
from werkzeug import generate_password_hash, check_password_hash
from sqlalchemy.ext.hybrid import hybrid_property


class User(db.Model):

    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    _password = db.Column(db.String(128))

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def _set_password(self, plaintext):
        self._password = bcrypt.generate_password_hash(plaintext)

    def is_active(self):
        return True

    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False

    def __repr__(self):
        return '<User %r>' % (self.email)


class Metric(db.Model):

    __tablename__ = 'metric'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), index=True)
    name = db.Column(db.String(64))
    is_bool = db.Column(db.Boolean)
    max_val = db.Column(db.Integer)
    min_val = db.Column(db.Integer)
    increment = db.Column(db.Integer)

    def __repr__(self):
        return '<Post %r>' % (self.name)


class Record(db.Model):

    __tablename__ = 'record'

    id = db.Column(db.Integer, primary_key=True)
    metric_id = db.Column(db.Integer, db.ForeignKey('metric.id'), index=True)
    value = db.Column(db.Integer)
    date = db.Column(db.DateTime)

    def __repr__(self):
        return '<Record %r>' % (self.value)
