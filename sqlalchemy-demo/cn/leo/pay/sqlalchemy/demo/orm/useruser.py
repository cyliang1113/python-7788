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
    
    def __str__(self):
        return u"UserUser(user_id=%d, user_name=%s)" % (self.user_id, self.user_name)