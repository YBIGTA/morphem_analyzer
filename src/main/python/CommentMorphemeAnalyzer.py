from konlpy.tag import Mecab
import os
# import subprocess

class CommentMorphemeAnalyzer:

    def __init__(self):
        self.load_dictionary()
        self.mecab = Mecab(os.path.dirname(os.path.abspath(__file__))+"/../../../mecab-ko-dic-2.0.1-20150920")

    def load_dictionary(self):
        os.system("bash " + os.path.dirname(os.path.abspath(__file__)) + "/../../../compile-dictionary.sh")

    # def load_common_dictionary(self):
    #     pass
    #
    # def load_webtoon_dictionary(self, webtoon_id):
    #     pass


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
