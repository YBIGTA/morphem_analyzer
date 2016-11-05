from .util import CommentDbConnector


class CommentMorphemAnalyzer:

    def __init__(self, jdbc_url, user_name, password, database):
        self.comment_db_connector = CommentDbConnector.CommentDbConnector(jdbc_url, user_name, password, database)

    def initialize(self):

    def load_dictionary(self, wetboon_id):

    def load_common_dictionary(self, wetboon_id):

    def load_webtoon_dictionary(self, wetboon_id):

    def analyze(self, comment):

    def analyze_comments(self, comments):
        analyzed_comments = [self.analze(comment) for comment in comments]
        return analyzed_comments
