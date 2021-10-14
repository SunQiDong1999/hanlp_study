from pyhanlp import *


def classic_demo():
    words = ["hers", "his", "she", "he"]
    map = JClass('java.util.TreeMap')()     # 创建TreeMap实例
    for word in words:
        map[word] = word.upper()            # 存放键值对
    trie = JClass('com.hankcs.hanlp.collection.AhoCorasick.AhoCorasickDoubleArrayTrie')(map)
    for hit in trie.parseText("ushers"):    # 遍历查询结果
        print("[%d:%d]=%s" % (hit.begin, hit.end, hit.value))


if __name__ == '__main__':
    classic_demo()
