import time

s: str = "abcdefgghijklmnopqrstuvwxyz"
b: bytes = bytes(s, 'ascii')

def one(start: int) -> str:
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

def two(start: int) -> str:
    arr: list[int] = [0] * 32
    tot: int = 0
    for i in range(len(b) - start):
        d: int = b[start+i] % 32
        if arr[d]:
            return two(i+1)
        
        arr[d] = 1
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

# two is 7x faster than one
