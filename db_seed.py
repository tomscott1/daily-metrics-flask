#!flask/bin/python
from app import db, models
from datetime import datetime, date, timedelta
# from .models import User, Metric, Record

# Clear existing users/metrics/records
users = models.User.query.all()
for u in users:
    db.session.delete(u)

metrics = models.Metric.query.all()
for m in metrics:
    db.session.delete(m)

records = models.Record.query.all()
for r in records:
    db.session.delete(r)

# Create Users
user1 = models.User(email='ralph@gmail.com', password='testtest')
user2 = models.User(email='garth@gmail.com', password='testtest')

# Add users to session and commit
db.session.add_all([user1, user2])
db.session.commit()

# Assign user ids to variables
user1_id = db.session.query(models.User.id).filter_by(email='ralph@gmail.com')
user2_id = db.session.query(models.User.id).filter_by(email='garth@gmail.com')

# Create metrics
metric1 = models.Metric(user_id=user1_id, name='Swimming', is_bool=True,
                        max_val=1, min_val=0, increment=1)
metric2 = models.Metric(user_id=user1_id, name='Mindfulness', is_bool=False,
                        max_val=10, min_val=1, increment=1)
metric3 = models.Metric(user_id=user2_id, name='Chinese', is_bool=True,
                        max_val=1, min_val=0, increment=1)
metric4 = models.Metric(user_id=user2_id, name='Peacefulness', is_bool=False,
                        max_val=10, min_val=1, increment=1)
metric5 = models.Metric(user_id=user2_id, name='Happiness', is_bool=False,
                        max_val=10, min_val=1, increment=1)

# Add metrics to session and commit
db.session.add_all([metric1, metric2, metric3, metric4, metric5])
db.session.commit()

# Get metric ids
metric1_id = db.session.query(models.Metric.id).filter_by(name='Swimming')
metric2_id = db.session.query(models.Metric.id).filter_by(name='Mindfulness')
metric3_id = db.session.query(models.Metric.id).filter_by(name='Chinese')
metric4_id = db.session.query(models.Metric.id).filter_by(name='Peacefulness')
metric5_id = db.session.query(models.Metric.id).filter_by(name='Happiness')

# Create dates for previous week
today = date.today()
todayl1 = today - timedelta(days=1)
todayl2 = today - timedelta(days=2)
todayl3 = today - timedelta(days=3)
todayl4 = today - timedelta(days=4)
todayl5 = today - timedelta(days=5)
todayl6 = today - timedelta(days=6)

# Create records for metric 1
r1 = models.Record(metric_id=metric1_id, value=1, date=todayl6)
r2 = models.Record(metric_id=metric1_id, value=0, date=todayl5)
r3 = models.Record(metric_id=metric1_id, value=1, date=todayl4)
r4 = models.Record(metric_id=metric1_id, value=0, date=todayl3)
r5 = models.Record(metric_id=metric1_id, value=0, date=todayl2)
r6 = models.Record(metric_id=metric1_id, value=1, date=todayl1)

# Add records to db
db.session.add_all([r1, r2, r3, r4, r5, r6])
db.session.commit()

# Create records for metric 2
r1 = models.Record(metric_id=metric2_id, value=8, date=todayl6)
r2 = models.Record(metric_id=metric2_id, value=4, date=todayl5)
r3 = models.Record(metric_id=metric2_id, value=3, date=todayl4)
r4 = models.Record(metric_id=metric2_id, value=7, date=todayl3)
r5 = models.Record(metric_id=metric2_id, value=9, date=todayl2)
r6 = models.Record(metric_id=metric2_id, value=10, date=todayl1)

# Add records to db
db.session.add_all([r1, r2, r3, r4, r5, r6])
db.session.commit()

# Create records for metric 3
r1 = models.Record(metric_id=metric3_id, value=0, date=todayl6)
r2 = models.Record(metric_id=metric3_id, value=1, date=todayl5)
r3 = models.Record(metric_id=metric3_id, value=1, date=todayl4)
r4 = models.Record(metric_id=metric3_id, value=1, date=todayl3)
r5 = models.Record(metric_id=metric3_id, value=0, date=todayl2)
r6 = models.Record(metric_id=metric3_id, value=1, date=todayl1)

# Add records to db
db.session.add_all([r1, r2, r3, r4, r5, r6])
db.session.commit()

# Create records for metric 4
r1 = models.Record(metric_id=metric4_id, value=1, date=todayl6)
r2 = models.Record(metric_id=metric4_id, value=5, date=todayl5)
r3 = models.Record(metric_id=metric4_id, value=6, date=todayl4)
r4 = models.Record(metric_id=metric4_id, value=2, date=todayl3)
r5 = models.Record(metric_id=metric4_id, value=9, date=todayl2)
r6 = models.Record(metric_id=metric4_id, value=8, date=todayl1)

# Add records to db
db.session.add_all([r1, r2, r3, r4, r5, r6])
db.session.commit()

# Create records for metric 5
r1 = models.Record(metric_id=metric5_id, value=4, date=todayl6)
r2 = models.Record(metric_id=metric5_id, value=7, date=todayl5)
r3 = models.Record(metric_id=metric5_id, value=1, date=todayl4)
r4 = models.Record(metric_id=metric5_id, value=1, date=todayl3)
r5 = models.Record(metric_id=metric5_id, value=5, date=todayl2)
r6 = models.Record(metric_id=metric5_id, value=6, date=todayl1)

# Add records to db
db.session.add_all([r1, r2, r3, r4, r5, r6])
db.session.commit()

# Log current database to console
users = models.User.query.all()
metrics = models.Metric.query.all()
records = models.Record.query.all()

print '--- Users ---'
for u in users:
    print(u.id, u.email, u.password)

print '--- Metrics ---'
for m in metrics:
    print(m.id, m.name, m.user_id)

print '--- Records ---'
for r in records:
    print(r.id, r.metric_id, r.value, r.date)
