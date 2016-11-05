from src.main.python.util import CommentDbConnector
from src.main.python.CommentLoader import CommentLoader
import yaml
import unittest
import logging

class TestDbConnection(unittest.TestCase):
    def setUp(self):
        logging.basicConfig(level=logging.INFO)

        self.configuration_path = "../resource/application.yml"
        with open(self.configuration_path, 'r') as fi:
            self.conf = self._load_configuration(fi)

    def _load_configuration(self, file):
        return yaml.load(file)

    def test_db_connection(self):
        comment_db_connector = CommentDbConnector(host=self.conf['host'],
                                                  port=self.conf['port'],
                                                  user_name=self.conf['user_name'],
                                                  password=self.conf['password'],
                                                  database=self.conf['database'])

        cur = comment_db_connector.get_cursor()
        cur.execute("select 1")

        self.assertIs(cur.fetchone()[0], 1)

    def test_db_comment_load(self):
        comment_loader = CommentLoader(host=self.conf['host'],
                                       port=self.conf['port'],
                                       user_name=self.conf['user_name'],
                                       password=self.conf['password'],
                                       database=self.conf['database'])

        comments = comment_loader.load_comments(self.conf['webtoon_id'], self.conf['episode_id'])
        self.assertIsNotNone(comments)


if __name__ == '__main__':
    unittest.main()
