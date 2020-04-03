def strSum(n: str):
    s = 0
    for i in n:
        s ^= ord(i)
    return s == 3
