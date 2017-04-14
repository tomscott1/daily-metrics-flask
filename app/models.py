from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)

    def __repr__(self):
        return '<User %r>' % (self.nickname)

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
