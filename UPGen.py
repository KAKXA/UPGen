from Crypto.Hash import SHA512, SHA224
from Base94 import Base94
from Contains import contains

while True:
    l = input('Enter length(between 1 and 256)(default 16):')
    if l == '': l = '16'
    if l.isdecimal() and (1 <= int(l) <= 256):
        l = int(l)
        break
k = input('Enter keyword:')
while True:
    t = input('Enter type(username(u) or password(p) or others(o))(default p):')
    if t == '': t = 'p'
    if t == 'u' or t == 'p' or t == 'o': break
while True:
    w = input('With punctuations(y/n)(default y):')
    if w == '': w = 'y'
    if w == 'y' or w == 'n': break
while True:
    d = input('Start with digits?(y/n)(default y)')
    if d == '': d = 'y'
    if d == 'y' or d == 'n': break
while True:
    s = input('Enter seed:')
    temp = SHA224.new()
    temp.update(s.encode())
    if temp.hexdigest() == 'c94eb266a5f574ffb9fcd8b9bfd7d731c8add531c2b8d10413584be3':
        break

m = k + t + s

a = SHA512.new()
a.update(s.encode())
b = a.digest()
res = Base94(b, withPunctuation= False if w == 'n' else True).decode()


for i in range(513 - l):
    if contains(res[i: l + i], withPunctuation= False if w == 'n' else True, startWithDigit= False if d == 'n' else True):
        print(res[i: l + i])
        break
