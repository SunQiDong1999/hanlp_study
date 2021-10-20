from pyhanlp import *
from jpype import JString


def load_from_file(path):
    """
    从词典文件中加载DoubleArrayTrie
    :param path: 词典路径
    :return: 双数组字典树
    """
    map = JClass('')