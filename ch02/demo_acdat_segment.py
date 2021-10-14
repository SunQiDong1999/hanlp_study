from pyhanlp import *

HanLP.Config.ShowTermNature = False
segment = JClass('com.hankcs.hanlp.seg.Other.AhoCorasickDoubleArrayTrieSegment')()
print(segment.seg("江西鄱阳湖干枯，中国最大淡水湖变成大草原"))
