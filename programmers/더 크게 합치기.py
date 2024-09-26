def solution(a, b):
    answer = 0
    q = str(a) + str(b)
    w = str(b) + str(a)
    if int(q) >= int(w):
        return int(q)
    else:
        return int(w)
    
print(solution(9, 91))