# coding: utf-8

# 要安装mysql-connector-python
# https://dev.mysql.com/doc/connector-python/en/connector-python-installation.html

import mysql.connector

dbConfig = {
    "user" : "root",
    "password" : "123456",
    "host" : "192.168.17.212",
    "database" : "x-back"
    }
conn = mysql.connector.connect(**dbConfig)
cursor = conn.cursor()
cursor.execute("select * from t_sys_menu")

for row in cursor:
    print row
    
cursor.close()
conn.close()
