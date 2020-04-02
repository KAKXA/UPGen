from random import randint
from string import digits, ascii_letters, punctuation


def strGen(length):
    root = digits + ascii_letters + punctuation
    rootLen = len(root) - 1
    temp = ''
    for i in range(length):
        temp += root[randint(0, rootLen)]
    return temp.encode()
