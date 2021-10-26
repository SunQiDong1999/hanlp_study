from pyhanlp import HanLP
from msr import msr_model
from ngram_segment import load_bigram, CoreDictionary

segment = load_bigram(model_path=msr_model, verbose=False, ret_viterbi=False)
assert CoreDictionary.contains("管道")
text = "北京输气管道工程"
HanLP.Config.enableDebug()
print(segment.seg(text))