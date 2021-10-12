from utility import *
from segment_algr import *
from speed_benchmark import *

dic = load_dictionary()
print("朴素的完全分词结果：")
print(fully_segment('商品和服务', dic))
print(fully_segment('就读北京大学', dic))
print("正向最长匹配分词结果：")
print(forward_segment('就读北京大学', dic))
print(forward_segment('研究生命起源', dic))
print("逆向最长匹配分词结果：")
print(backward_segment('研究生命起源', dic))

test_list = [
    "项目的研究",
    "商品和服务",
    "研究生命起源",
    "当下雨天地面积水",
    "结婚的和尚未结婚的",
    "欢迎新老师生前来就餐",
]
print("双向最长匹配分词结果：")
for sentence in test_list:
    print(bidirectional_segment(sentence, dic))

evaluate_speed(forward_segment, "江西鄱阳湖干枯，中国最大淡水湖变成草原", dic, 10000)
evaluate_speed(backward_segment, "江西鄱阳湖干枯，中国最大淡水湖变成草原", dic, 10000)
evaluate_speed(bidirectional_segment, "江西鄱阳湖干枯，中国最大淡水湖变成草原", dic, 10000)
