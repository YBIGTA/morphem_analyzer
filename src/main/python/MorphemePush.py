import logging
from .util import CommentDbConnector


class MorphemePush:
    _push_morpheme_query_format = "insert into comment_morpheme_analyzed " \
                                  + "  (title_id, episode_no, comment_no, morpheme, morpheme_tag, morpheme_location)" \
                                  + "  values "

    _push_morpheme_query_values_format = "(%d, %d, %d, '%s', '%s', %d)"

    def __init__(self, host, port, password, database, user_name):
        self.comment_db_connector = CommentDbConnector(host, port, user_name, password, database)

    def push_morphemes(self, analyzed_comments):
        con = self.comment_db_connector.get_con()
        cur = con.cursor()

        count = 0

        for comment in analyzed_comments:
            logging.info("webtoon_id : {webtoon_id}, episode_id : {episode_id}".format(
                webtoon_id=comment[0][0], episode_id=comment[0][1]))

            values = [self._push_morpheme_query_values_format % (
                morpheme[0], morpheme[1], morpheme[2], morpheme[3], morpheme[4], morpheme[5]) for morpheme in
                      comment]

            query = self._push_morpheme_query_format + ",".join(values)

            try:
                print(count)
                cur.execute(query)
                count += len(comment)
                con.commit()
            except cur.Error as err:
                print("input error query: {}".format(query))
                print("{}", err)

        return count
