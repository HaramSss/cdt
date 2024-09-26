def solution(a, b):
    answer = 0
    plus = str(a) + str(b)
    m = 2 * a * b
    if int(plus) >= m:
        return int(plus)
    else:
        return m

print(solution(2, 91))