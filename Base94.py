# 从十六进制有损编码到94个西文键盘字符
from string import digits, ascii_letters, punctuation


def Base94(s: bytes, withPunctuation = True) -> bytes:
    f = digits + ascii_letters

    if withPunctuation:
        f = (digits + ascii_letters + punctuation)

    fLen = len(f)
    blockSize = 231
    l = len(s)
    if l & (l - 1) != 0:
        raise Exception('The length of the input bytes is not the power of two.')
    s = int((s * blockSize).hex(), 16)
    res = ''
    for i in range(l * 8):
        res = f[(s & ((1 << blockSize) - 1)) % fLen] + res
        s >>= blockSize
    return res.encode()


'''
#Theory base: block size = 231
from math import sqrt
from Crypto.Hash import SHA512
def isPrime(a):
    for i in range(2, int(sqrt(a) + 1)):
        if a % i == 0:
            return False
    return True

l = [2 ** (2 * i + 5)for i in range(50)]
min = []
for i in range(65536):
    if isPrime(i):
        m1 = abs((1 << (2 * i + 5)) % 94 - 47)
        m2 = abs((1 << (2 * i + 5)) % 62 - 31)

        if m1 == 45 and m2 == 29:
            min.append(2 * i + 5)
print(min)
'''

'''
from StringGenerator import strGen
f = (digits + ascii_letters + punctuation)
mapp = dict(zip(list(f), ([0] * 94)))
for i in range(1):
    a = Base94(strGen(512))
    for i in a.decode():
        mapp[i] += 1

print(mapp)
'''
