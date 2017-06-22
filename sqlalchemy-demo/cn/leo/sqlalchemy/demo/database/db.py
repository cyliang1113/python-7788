# coding: utf-8

from  sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+mysqlconnector://root:123456@192.168.17.212:3306/python-demo?charset=utf8', echo=False)

dbsession_maker = sessionmaker(bind=engine)

get_session = dbsession_maker

print "db.py"
