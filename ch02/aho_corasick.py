from pyhanlp import *


def classic_demo():
    words = ["hers", "his", "she", "he"]
    Trie = JClass('com.hankcs.hanlp.algorithm.ahocorasick.trie.Trie')
    trie = Trie()
    for w in words:
        trie.addKeyword(w)

    for emit in trie.parseText("ushers"):
        print("[%d:%d]=%s" % (emit.getStart(), emit.getEnd(), emit.getKeyword()))


if __name__ == '__main__':
    classic_demo()
