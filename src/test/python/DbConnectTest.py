from src.main.python.util import CommentDbConnector

import yaml
import unittest


class TestDbConnection(unittest.TestCase):
    def setUp(self):
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


if __name__ == '__main__':
    unittest.main()
