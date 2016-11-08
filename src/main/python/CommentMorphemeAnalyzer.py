from konlpy.tag import Mecab
import os
import subprocess

class CommentMorphemeAnalyzer:

    def __init__(self):
        self.mecab = Mecab()


    # def initialize(self):


    def load_dictionary(self, webtoon_id):
        # 밑의 로드 메소드로 사전을 복사하고
        self.load_common_dictionary()
        # if 해당 웹툰의 딕셔너리가 있는 경우 또 복사,
        self.load_webtoon_dictionary(webtoon_id)

        # 여기서 반영?
        os.system("bash ../../compile-dictionary")

    def load_common_dictionary(self):
        pass

    def load_webtoon_dictionary(self, webtoon_id):
        pass


    def analyze(self, comment):
        info_list = comment[:3]
        morpheme_list = self.mecab.pos(comment[3])
        result = []
        for location, morpheme in enumerate(morpheme_list):
            row = list(info_list) + list(morpheme)
            row.append(location)
            result.append(row)
        return result

    def analyze_comments(self, comments):
        analyzed_comments = [self.analyze(comment) for comment in comments]
        return analyzed_comments
    """
        return form
        [
            [comments 1 :
                [morpheme정보1], [morpheme정보2], ... [morpheme정보n]
            ]
            [comments 2 :
                [morpheme정보1], [morpheme정보2], ... [morpheme정보n]
            ]
        ]

    """
