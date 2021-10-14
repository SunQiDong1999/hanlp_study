from pyhanlp import *
from pyhanlp.static import HANLP_DATA_PATH

HanLP.Config.ShowTermNature = False
segment = DoubleArrayTrieSegment()
print(segment.seg('江西鄱阳湖干枯，中国最大淡水湖变成大草原'))

dict1 = HANLP_DATA_PATH + "/dictionary/CoreNatureDictionary.mini.txt"
dict2 = HANLP_DATA_PATH + "/dictionary/custom/上海地名.txt ns"
segment = DoubleArrayTrieSegment([dict1, dict2])
print(segment.seg('上海市虹口区大连西路550号SISU'))

segment.enablePartOfSpeechTagging(True)
HanLP.Config.ShowTermNature = True
print(segment.seg('上海市虹口区大连西路550号SISU'))

for term in segment.seg('上海市虹口区大连西路550号SISU'):
    print("单词:%s 词性:%s" % (term.word, term.nature))