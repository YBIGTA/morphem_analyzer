import logging
from .util import CommentDbConnector


class MorphemePush:
    _push_morpheme_query_format = "insert into comment_morpheme_analyzed" \
                                  + " (title_id, episode_no, comment_no, morpheme, morpheme_tag, morpheme_location)" \
                                  + " values "

    _push_morpheme_query_values_format = "(%d, %d, %d, '%s', '%s', %d)"

    def __init__(self, host, port, password, database, user_name):
        try:
            self.comment_db_connector = CommentDbConnector(host, port, user_name, password, database)
        except:
            print("connect failed")

    def push_morphemes(self, analyzed_comments):
        con = self.comment_db_connector.get_con()
        cur = con.cursor()

        count = 0

        for comment in analyzed_comments:

            values = [self._push_morpheme_query_values_format % (
                morpheme[0], morpheme[1], morpheme[2], morpheme[3], morpheme[4], morpheme[5]) for morpheme in
                      comment]

            query = self._push_morpheme_query_format + ",".join(values)

            try:
                if count % 1000 is 0:
                    logging.info("%d done" % count)
                    print("%d pushed" % count)
                cur.execute(query)
                count += len(comment)
                con.commit()
            except cur.Error as err:
                # logging.error("input error query: {}".format(query))
                logging.error("{}".format(err))
                logging.error(values)

        return count
