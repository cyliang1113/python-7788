# coding: utf-8

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from sqlalchemy import Column, Integer, String

class UserUser(Base):
    __tablename__ = 't_user_user'
    user_id = Column(Integer, primary_key=True)
    user_no = Column(String, nullable=True)
    city_id = Column(String, nullable=True)
    user_name = Column(String)
    user_password = Column(String, nullable=True)
    
    def __init__(self, name):
        self.user_name = name




