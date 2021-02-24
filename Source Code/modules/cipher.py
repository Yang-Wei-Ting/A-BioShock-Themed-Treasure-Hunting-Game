def decrypt(text, s=-3):
    res = []
    for c in text:
        if c.isupper():
            res.append(chr((ord(c) + s - 65) % 26 + 65))
        elif c.islower():
            res.append(chr((ord(c) + s - 97) % 26 + 97))
        else:
            res.append(c)
    return "".join(res)
