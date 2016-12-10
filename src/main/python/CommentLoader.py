import pymysql
import logging
from .util import CommentDbConnector


class CommentLoader:
    _get_comment_count_query = "select count(*) from comment " \
                               + " where title_id = %s " \
                               + " and episode_no= %s "
    _get_comment_query = "select * from comment " \
                         + " where title_id = %s " \
                         + " and episode_no = %s "

    def __init__(self, host, port, password, database, user_name):
        self.comment_db_connector = CommentDbConnector(host, port, user_name, password, database)

    def load_comments(self, webtoon_id, episode_id_li):
        result = []
        for episode_id in episode_id_li:
            episode_id = int(episode_id)
            logging.info("webtoon_id : {webtoon_id}, episode_id : {episode_id} ".format(
                webtoon_id=webtoon_id, episode_id=episode_id))

            comment_size = self.get_comments_size(webtoon_id, episode_id)

            logging.info("webtoon_id : {webtoon_id}, episode_id : {episode_id}, comment size : {comment_size}".format(
                webtoon_id=webtoon_id, episode_id=episode_id, comment_size=comment_size[0]))

            cur = self.comment_db_connector.get_cursor()
            cur.execute(self._get_comment_query % (webtoon_id, episode_id))

            result += list(cur.fetchall())
            print("webtoon_id : {webtoon_id}, episode_id : {episode_id} loaded".format(
                webtoon_id=webtoon_id, episode_id=episode_id))

        return result

    def get_comments_size(self, webtoon_id, episode_id):
        cur = self.comment_db_connector.get_cursor()
        cur.execute(self._get_comment_count_query % (webtoon_id, episode_id))
        webtoon_comment_count = cur.fetchone()
        return webtoon_comment_count
