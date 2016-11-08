from src.main.python.CommentLoader import CommentLoader
from src.main.python.CommentMorphemeAnalyzer import CommentMorphemeAnalyzer
from src.main.python.MorphemePush import MorphemePush


if __name__ == "__main__":
    host = input("host name :")
    port = int(input("port :"))
    user_name = input("user_name :")
    password = input("password :")
    database = input("database :")

    cl = CommentLoader(host, port, password, database, user_name)



    webtoon_id = int(input("webtoon_id :"))
    episode_id = int(input("episode_id :"))

    comments_loaded = cl.load_comments(webtoon_id, episode_id)
    cma = CommentMorphemeAnalyzer()

    morpheme_analyzed = cma.analyze_comments(comments_loaded)

    mp = MorphemePush(host, port, password, database, user_name)
    num_push = mp.Push_morphemes(morpheme_analyzed)


    print("success! Morpheme number = ", num_push)

"""
host: 175.158.15.40
port: 3308
user_name: ybigta
password: ybigta
database: webtoon
webtoon_id: 20853
episode_id: 1059
"""








