import pymysql

"""
host = "175.158.15.40"
user_name = "ybigta"
password =  "ybigta"
database= "webtoon"
port=3308
"""

class CommentDbConnector:

    def __init__(self, host, port, user_name, password, database):
        self.host = host
        self.port = port
        self.user_name = user_name
        self.password = password
        self.database = database

    def get_con(self):
        self.con = pymysql.connect(host=self.host,
                              port=self.port,
                              user=self.user_name,
                              password=self.password,
                              database=self.database,
                              use_unicode=True,
                              charset='utf8')
        return self.con

    def get_cursor(self):
        self.get_con()
        self.con.autocommit_mode = True
        cur = self.con.cursor()
        return cur
