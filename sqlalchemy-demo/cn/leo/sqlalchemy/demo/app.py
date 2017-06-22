# coding: utf-8

from cn.leo.sqlalchemy.demo.database.db import get_session

from cn.leo.sqlalchemy.demo.orm.models import UserUser

session1 = get_session()
print session1

user_user_list = session1.query(UserUser).all()

for user_user in user_user_list:
    print user_user.user_id, user_user.user_name

session1.close()

# session2 = get_session()
session2 = session1
print session2
user = UserUser(u"爱国者")
session2.add(user)
session2.commit()




