import pymysql
import logging


class CommentLoader:
    _get_comment_count_query = "select count(*) from tb_comment " \
                               + " where webtoon_id = %s " \
                               + " and episode_id= %s "
    _get_comment_query = "select * from tb_comment " \
                         + " where webtoon_id = %s " \
                         + " and episode_id = %s "

    def __init__(self, jdbc_url, user_name, password, database):
        self.jdbc_url = jdbc_url
        self.user_name = user_name
        self.password = password
        self.database = database

    def load_comments(self, webtoon_id, episode_id):
        logging.info("webtoon_id : {webtoon_id}, episode_id : {episode_id} ".format(
            {webtoon_id: webtoon_id, episode_id: episode_id}))

        comment_size = self.get_comments_size(webtoon_id, episode_id)

        logging.info("webtoon_id : {webtoon_id}, episode_id : {episode_id}, comment size : {comment_size}".format(
            {webtoon_id: webtoon_id, episode_id: episode_id, comment_size: comment_size}))

        cur = self._get_cursor()
        cur.execute(self._get_comment_query % (webtoon_id, episode_id))
        return cur.fetchall()


    def get_comments_size(self, webtoon_id, episode_id):
        cur = self.get_cursor()
        cur.execute(self._get_comment_count_query % ( webtoon_id, episode_id))
        webtoon_comment_count = cur.fetchone()
        return webtoon_comment_count

    def _get_cursor(self):
        con = pymysql.connect(host=self.jdbc_url, user=self.user_name, password=self.password, database=self.database)
        con.autocommit_mode = True
        cur = con.cursor()
        return cur
