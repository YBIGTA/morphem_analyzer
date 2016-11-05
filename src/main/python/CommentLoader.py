import pymysql
import logging
from .util import CommentDbConnector

class CommentLoader:
    _get_comment_count_query = "select count(*) from tb_comment " \
                               + " where webtoon_id = %s " \
                               + " and episode_id= %s "
    _get_comment_query = "select * from tb_comment " \
                         + " where webtoon_id = %s " \
                         + " and episode_id = %s "

    def __init__(self, jdbc_url, user_name, password, database):
        self.comment_db_connector = CommentDbConnector.CommentDbConnector(jdbc_url, user_name, password, database)


    def load_comments(self, webtoon_id, episode_id):
        logging.info("webtoon_id : {webtoon_id}, episode_id : {episode_id} ".format(
            {webtoon_id: webtoon_id, episode_id: episode_id}))

        comment_size = self.get_comments_size(webtoon_id, episode_id)

        logging.info("webtoon_id : {webtoon_id}, episode_id : {episode_id}, comment size : {comment_size}".format(
            {webtoon_id: webtoon_id, episode_id: episode_id, comment_size: comment_size}))

        cur = self.comment_db_connector.get_cursor()
        cur.execute(self._get_comment_query % (webtoon_id, episode_id))
        return cur.fetchall()

    def get_comments_size(self, webtoon_id, episode_id):
        cur = self.get_cursor()
        cur.execute(self._get_comment_count_query % (webtoon_id, episode_id))
        webtoon_comment_count = cur.fetchone()
        return webtoon_comment_count
