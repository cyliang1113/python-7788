# coding: utf-8

from cn.leo.sqlalchemy.demo.database.db import get_new_session

from cn.leo.sqlalchemy.demo.orm.models import UserUser

session = get_new_session()
print session

user_user_list = session.query(UserUser).all()

for user_user in user_user_list:
    print user_user.user_id, user_user.user_name

session.close()




