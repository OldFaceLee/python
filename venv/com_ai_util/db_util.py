# -*- encoding= utf-8 -*-

"""
@Author lixuejun
@Time 2020/5/18
"""

import pymysql   # python2.7 用pymysql, 如果是3.x 用MYSQLdb

class mysql_util:

    def __init__(self):
        pass

    def connect(self):
        conn = pymysql.connect(
            host="localhost",
            port=3306,
            user='root',
            passwd='cashc0wA',
            db='oldface',
            charset='utf8'
        )
        return conn

    def select(self, sql):
        my = mysql_util()
        cursor = my.connect().cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        print("执行的sql: %s , 查询到的数据：%s" % (sql, result))
        return result


instance = mysql_util()
sql_input = input("输入sql进行查询语句：")
instance.select(sql_input)








