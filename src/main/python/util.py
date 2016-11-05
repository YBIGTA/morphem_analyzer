import pymysql


class CommentDbConnector:

    def __init__(self, host, port, user_name, password, database):
        self.host = host
        self.port = port
        self.user_name = user_name
        self.password = password
        self.database = database

    def get_cursor(self):
        con = pymysql.connect(host=self.host,
                              port=self.port,
                              user=self.user_name,
                              password=self.password,
                              database=self.database,
                              use_unicode=True,
                              charset='utf8')

        con.autocommit_mode = True
        cur = con.cursor()
        return cur
