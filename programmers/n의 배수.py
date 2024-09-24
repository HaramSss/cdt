def solution(num, n):
    answer = 0
    if num % n == 0:
        return 1
    return 0

print(solution(98, 2))