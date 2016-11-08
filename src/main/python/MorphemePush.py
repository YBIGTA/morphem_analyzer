import logging
from .util import CommentDbConnector

class MorphemePush:
    _push_morpheme_query = "insert into comment_morpheme_analyzed " \
                         + "  (title_id, episode_no, comment_no, morpheme, morpheme_tag, morpheme_location)" \
                         + "  values (%d, %d, %d, '%s', '%s', %d)"


    def __init__(self, host, port, password, database, user_name):
        self.comment_db_connector = CommentDbConnector(host, port, user_name, password, database)

    def Push_morphemes(self, analyzed_comments):
        cur = self.comment_db_connector.get_cursor()

        count = 0
        for comment in analyzed_comments:
            logging.info("webtoon_id : {webtoon_id}, episode_id : {episode_id}".format(
                webtoon_id=comment[0][0], episode_id=comment[0][1]))
            for morpheme in comment:
                try:
                    cur.execute(self._push_morpheme_query %(morpheme[0], morpheme[1], morpheme[2], morpheme[3], morpheme[4], morpheme[5]))
                    count += 1
                except cur.Error as err:
                    print("input error: {}".format(err))
                    return 0
        cur.commit()
        return count
