from pyhanlp import *


class DoubleArrayTrie(object):
    def __init__(self, dic: dict) -> None:
        m = JClass('java.util.TreeMap')()
        for k, v in dic.items():
            m[k] = v
        DoubleArrayTrie = JClass('com.hankcs.hanlp.collection.trie.DoubleArrayTrie')
        dat = DoubleArrayTrie(m)
        self.base = dat.getBase()
        self.check = dat.getCheck()
        self.value = dat.getValueArray([''])

    @staticmethod
    def char_hash(c) -> int:
        return JClass('java.lang.Character')(c).hashCode()

    def transition(self, c, b) -> int:
        """
        状态转移
        :param c:字符
        :param b: 初始状态
        :return: 转移后的状态，-1表示失败
        """
        p = self.base[b] + self.char_hash(c) + 1
        if self.base[b] == self.check[p]:
            return p
        else:
            return -1

    def __getitem__(self, key: str):
        b = 0
        for i in range(0, len(key)):
            p = self.transition(key[i], b)
            if p is not -1:
                b = p
            else:
                return None

        p = self.base[b]
        n = self.base[p]
        if p == self.check[p] and n < 0:
            index = -n - 1
            return self.value[index]
        return None


if __name__ == '__main__':
    dic = {
        '自然': 'nature',
        '自然人': 'human',
        '自然语言': 'language',
        '自语': 'talk to oneself',
        '入门': 'introduction',
    }
    dat = DoubleArrayTrie(dic)
    print(dat['自然'] == 'nature')
    print(dat['自然语言'] == 'language')
    print(dat['不存在'] is None)
