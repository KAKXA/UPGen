#! /bin/python3
from pyperclip import copy
from getpass import getpass
from Crypto.Hash import SHA512
from Base94 import Base94
from Contains import contains
from StringSum import strSum
from Alias import alias

def inputR(output, default=None, f=None, hide=False):
    newInput = getpass if hide else input
    while True:
        if not default:
            temp = newInput(output + ':')
        elif default:
            temp = newInput(output + '(default(' + default + ')):')
            if temp == '':
                temp = default
        if not f or f(temp):
            return temp

t = inputR('Enter type(id(i)password(p)name(n))',default='p', f=lambda x: x in {'i','p','n'})
k = inputR('Enter keyword', default=None, f=None)
if t == 'n':
    m = k + t
else:
    d = inputR('Do not ban starting with a digit?(y/n)', default='y', f=lambda x: x in {'y','n'})
    swd = False if d == 'n' else True
    l = int(inputR('Enter length(between 6 and 256)', default='16', f=lambda x: int(x) in range(6, 257)))
    if t == 'p':
        w = inputR('With punctuations(y/n)', default='y', f=lambda x: x in {'y','n'})
        wp = False if w == 'n' else True
        s = inputR('Enter seed',default=None,f=strSum, hide=True)
        m = k + t + s
    elif t == 'i':
        w = inputR('With punctuations(y/n)', default='n', f=lambda x: x in {'y','n'})
        wp = False if w == 'n' else True
        m = k + t
        v = inputR('Old version?(y/n)', default='n', f=lambda x: x in {'y','n'})
        m = k + t if v == 'n' else k + 'u'
        

h = SHA512.new()
h.update(m.encode())

if t == 'i' or t == 'p':
    b = h.digest()
    string = Base94(b, wp).decode()
    for i in range(513 - l):
        res = string[i: l + i]
        if contains(res, withPunctuation=wp, startWithDigit=swd):
            break
elif t == 'n':
    res = alias(int(h.hexdigest(),16))
copy(res)
print('Already copy it to clipboard.')


'''
while True:
    t = input('Enter type(id(i) or password(p) or name(n))(default p):')
    if t == '': t = 'p'
    if t == 'i' or t == 'p' or t == 'n': break

while True:
    l = input('Enter length(between 1 and 256)(default 16):')
    if l == '': l = '16'

    if l.isdecimal() and (1 <= int(l) <= 256):
        l = int(l)
        break

k = input('Enter keyword:')

while t == 'i' or t == 'p':
    w = input('With punctuations(y/n)(default y for p and default n for i):')
    if w == '' and t == 'p': w = 'y'
    elif w == '' and t == 'i': w = 'n'
    if w == 'y' or w == 'n': break

while t == 'i' or t == 'p':
    d = input('Start with digits?(y/n)(default y)')
    if d == '': d = 'y'
    if d == 'y' or d == 'n': break

while t == 'p':
    s = getpass('Enter seed:')
    # 仅仅通过对输入串求和来判断输入的正确性,这一步的目的是为了提供防止输入失误的功能而不是防止不知seed者进入下一步;仅仅给出输入串的异或和,提供的信息量很少,可以防止攻击
    if strSum(s):
        m = k + t + s
        break
# if not a password, don't use seed to construct a result
if t == 'i' or t == 'n':
    m = k + t

a = SHA512.new()
a.update(m.encode())

if t == 'i' or t == 'p':
    b = a.digest()
    res = Base94(b, withPunctuation=False if w == 'n' else True).decode()
    for i in range(513 - l):
        if contains(res[i: l + i], withPunctuation= False if w == 'n' else True, startWithDigit= False if d == 'n' else True):
            copy(res[i: l + i])
            print('Already copy it to clipboard.')
            break
elif t == 'n':
    b = int(a.hexdigest(),16)
    copy(b)
    print('Already copy it to clipboard.')
    '''

