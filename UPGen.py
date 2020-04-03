#! /bin/python3
from Crypto.Hash import SHA512
from Base94 import Base94
from Contains import contains
from StringSum import strSum

while True:
    t = input('Enter type(username(u) or password(p) or others(o))(default p):')
    if t == '': t = 'p'
    if t == 'u' or t == 'p' or t == 'o': break

while True:
    l = input('Enter length(between 1 and 256)(default 16):')
    if l == '': l = '16'

    if l.isdecimal() and (1 <= int(l) <= 256):
        l = int(l)
        break

k = input('Enter keyword:')

while True:
    w = input('With punctuations(y/n)(default y for p and default n for u and o):')
    if w == '' and t == 'p': w = 'y'
    elif w == '' and (t == 'u' or t == 'o'): w = 'n'
    if w == 'y' or w == 'n': break
while True:
    d = input('Start with digits?(y/n)(default y)')
    if d == '': d = 'y'
    if d == 'y' or d == 'n': break

while t == 'p':
    s = input('Enter seed:')
    # 仅仅通过对输入串求和来判断输入的正确性,这一步的目的是为了提供防止输入失误的功能而不是防止不知seed者进入下一步;仅仅给出输入串的异或和,提供的信息量很少,可以防止攻击
    if strSum(s):
        global m
        m = k + t + s
        break


# if not a password, don't use seed to construct a result
if t == 'u' or t == 'o':
    m = k + t

a = SHA512.new()
a.update(m.encode())
b = a.digest()
res = Base94(b, withPunctuation=False if w == 'n' else True).decode()


for i in range(513 - l):
    if contains(res[i: l + i], withPunctuation= False if w == 'n' else True, startWithDigit= False if d == 'n' else True):
        print(res[i: l + i])
        break
