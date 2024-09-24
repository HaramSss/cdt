def solution(num_list):
    a = 1
    b = 0
    for i in num_list:
        a = a * i
    for i in num_list:
        b = b + i
    if a < b*b :
        return 1
    else :
        return 0


def solution(num_list):
    a=1
    b=0
    for x in num_list:
        a*=x
        b+=x
    if a<b*b: return 1
    return 0

print(solution([3, 4, 5, 2, 1]))