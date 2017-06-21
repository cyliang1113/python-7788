# coding: utf-8

from sqlalchemy.ext.declarative import declarative_base
from __builtin__ import True

Base = declarative_base()

from sqlalchemy import Column, Integer, String

class UserUser(Base):
    __tablename__ = 't_user_user'
    user_id = Column(Integer, primary_key=True)
    user_no = Column(String)
    city_id = Column(String)
    user_name = Column(String)
    user_password = Column(String)
    
    
from  sqlalchemy import create_engine
engine = create_engine('mysql+mysqlconnector://root:123456@192.168.17.212:3306/python-demo?charset=utf8')

from sqlalchemy.orm import sessionmaker
DBSession = sessionmaker(bind=engine)

session = DBSession()
user_user_list = session.query(UserUser).all()

for user_user in user_user_list:
    print user_user.user_id, user_user.user_name

session.close()



