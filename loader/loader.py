# -*- coding: utf-8 -*-
from google.appengine.ext import db
from google.appengine.tools import bulkloader
from model import Lecture

class LectureLoader(bulkloader.Loader):
  def __init__(self):
    bulkloader.Loader.__init__(self, 'Lecture',
                               [('lecture_no', int),
                                ('lecture_title', lambda x: x.decode('utf-8')),
                                ('lecture_date', lambda x: x.decode('utf-8'))
                               ])

  def generate_key(self, i, values):
    return values[0]



loaders = [LectureLoader]
