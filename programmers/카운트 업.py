def solution(start_num, end_num):
    answer = []
    a = int(start_num)
    b = int(end_num)
    for i in range(a, b+1):
        answer.append(i)
    return answer

print(solution(3, 10))

# def solution(start, end):
#     return list(range(start, end + 1))