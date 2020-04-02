from string import digits, ascii_lowercase, ascii_uppercase, punctuation


def contains(s: str, withPunctuation = True, startWithDigit = True) -> bool:
    setD = set(digits.strip())
    setL = set(ascii_lowercase.strip())
    setU = set(ascii_uppercase.strip())
    setP = set(punctuation.strip())

    tagD = False
    tagL = False
    tagU = False
    tagP = False

    if s[0] in setD and not startWithDigit:
        return False
    for i in range(len(s)):
        if s[i] in setD: tagD = True
        elif s[i] in setL: tagL = True
        elif s[i] in setU: tagU = True
        elif s[i] in setP: tagP = True

    if tagD and tagL and tagU and tagP and withPunctuation:
        return True
    elif tagD and tagL and tagU and not withPunctuation:
        return True
    return False
