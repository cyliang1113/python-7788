# coding: utf-8

from  sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import cn.leo.sqlalchemy.demo.config.database_config as database_config

engine = create_engine(database_config.url, echo=False)

dbsession_maker = sessionmaker(bind=engine)

get_session = dbsession_maker

print "db.py"
