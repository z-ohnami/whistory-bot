# -*- coding: utf-8 -*-
import random
from google.appengine.ext import db
from model import Lecture
from model import LectOrder
import logging

SITE_URL = "http://www.geocities.jp/timeway/"
KOUGI_NUM = 106

def getMsg():
    lecture_no = lectorder_get()

    query = db.GqlQuery("SELECT * FROM Lecture WHERE lecture_no = :1",lecture_no)
    rec = query.get()

    msg = u"-世界史講義録より- \n" + rec.lecture_title + "\n" + SITE_URL + "kougi-" + str(lecture_no) + ".html"

    return msg

def lectorder_init():
   query = LectOrder.all()
   if query.count() > 0:
      rec = query.get()
      db.delete(rec)

   obj = LectOrder()
   for i in range(1,KOUGI_NUM + 1):
      obj.lecture_order.append(i)
   random.shuffle(obj.lecture_order)
   db.put(obj)

def lectorder_get():
   query = LectOrder.all()
   rec = query.get()

   if rec == None or len(rec.lecture_order) == 0:
      lectorder_init()
      query = LectOrder.all()
      rec = query.get()

   no = rec.lecture_order.pop()
   db.put(rec)

   return no

def main():
    print getMsg()

if __name__ == "__main__":
    main()
