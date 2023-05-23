import time

s: str = "abcdefghijklmnopqrstuvwxyz"

def one(start: int):
    data: dict[str, int] = {}
    tot: int = 0
    if start >= len(s):
        return ""
    for i in range(len(s)):
        if s[i] in data:
            return one(start+1)
        else:
            data[s[i]] = 0
            tot += 1
            if tot == 14:
                return s[start:tot+start]
    return ""

def two(start: int):
    data: dict[str, int] = {}
    tot: int = 0
    if start >= len(s):
        return ""
    for i in range(len(s) - start):
        if s[start+i] in data:
            return two(i+1)
        else:
            data[s[start+i]] = 0
            tot += 1
            if tot == 14:
                return s[start:tot+start]
    return ""

st: float = time.time()
print(one(0))
t1: float = time.time()-st

st: float = time.time()
print(two(0))
t2: float = time.time()-st
print(t2)

print(t1/t2)

# two is 5x faster than one
