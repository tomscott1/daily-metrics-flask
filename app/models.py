from app import db
from werkzeug import generate_password_hash, check_password_hash

class User(db.Model):

    def __repr__(self):
        return '<User %r>' % (self.nickname)

    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True, nullabl=F)

    # password
    _password = db.Column('password', db.String(120), nullable=False)

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

    def _get_password(self):
        return self._password

    def _set_password(self, password):
        self._password = generate_password_hash(password)

    password = db.synonym('_password', description=property(_get_password, _set_password))

    def check_password(self, password):
        if self.password is None:
            return False
        return check_password_hash(self.password, password)

    # methods
    @classmethod
    def authenticate(cls, email, password):
        user = User.query.filter(db.or_(User.email == email)).first()

        if user:
            is_authenticated = user.check_password(password)
        else:
            is_authenticated = False
        return user, is_authenticated

    @classmethod
    def is_email_taken(cls, email_address):
        return db.session.query(db.exists().where(USer.email == email_address)).scalar()



class Metric(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'), index=True)
    name = db.Column(db.String(64))
    is_bool = db.Column(db.Boolean)
    max_val = db.Column(db.Integer)
    min_val = db.Column(db.Integer)
    increment = db.Column(db.Integer)

    def __repr__(self):
        return '<Post %r>' % (self.name)


class Record(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    metric_id = db.Column(db.Integer, db.ForeignKey('Metric.id'), index=True)
    value = db.Column(db.Integer)
    date = db.Column(db.DateTime)

    def __repr__(self):
        return '<Record %r>' % (self.value)
