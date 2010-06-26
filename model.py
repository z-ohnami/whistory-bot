from google.appengine.ext import db

class Lecture(db.Model):
  lecture_no = db.IntegerProperty()
  lecture_title = db.StringProperty()
  lecture_date = db.StringProperty()

class LectOrder(db.Model):
  lecture_order = db.ListProperty(int)

