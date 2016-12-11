from src.main.python.CommentLoader import CommentLoader
from src.main.python.CommentMorphemeAnalyzer import CommentMorphemeAnalyzer
from src.main.python.MorphemePush import MorphemePush
import yaml
import os
import logging
import re


def load_configuration():
    configuration_path = os.path.dirname(os.path.abspath(__file__)) + "/../resource/application.yml"

    def _load_configuration(file):
        return yaml.load(file)

    with open(configuration_path, 'r') as fi:
        return _load_configuration(fi)


def run():
    logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s', filename='morpheme.log', level=logging.INFO)
    conf = load_configuration()

    print("load pring loader")
    cl = CommentLoader(host=conf['host'],
                       port=conf['port'],
                       user_name=conf['user_name'],
                       password=conf['password'],
                       database=conf['database'])

    webtoon_id = int(input("webtoon_id :"))
    episode_id = input("episode_id (delimeter=','):")
    episode_id_li = re.compile('[, ]+').split(episode_id)
    print(episode_id_li)

    print("load comment done")
    comments_loaded = cl.load_comments(webtoon_id, episode_id_li)

    # print("load morpheme analyzer", cl.get_comments_size(webtoon_id, episode_id))
    cma = CommentMorphemeAnalyzer()
    print("load done morpheme analyzer")

    morpheme_analyzed = cma.analyze_comments(comments_loaded)
    print("analysis done")

    mp = MorphemePush(host=conf['host'],
                      port=conf['port'],
                      user_name=conf['user_name'],
                      password=conf['password'],
                      database=conf['database'])
    num_push = mp.push_morphemes(morpheme_analyzed)

    print("success! Morpheme number = ", num_push)


if __name__ == "__main__":
    run()

"""
host: 175.158.15.40
port: 3308
user_name: ybigta
password: ybigta
database: webtoon
webtoon_id: 20853
episode_id: 1059
"""
