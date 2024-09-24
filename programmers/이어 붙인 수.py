def solution(num_list):
    answer1 = ""
    answer2 = ""
    for i in num_list:
        if i % 2 != 0:
            answer1 += str(i)
        else:
            answer2 += str(i)
    answer = int(answer1) + int(answer2)
    return answer


def solution(num_list):
    answer = 0
    a=""#홀수
    b=""#짝수
    for i in num_list:
        if i%2!=0:
            a+=str(i)
        else:
            b+=str(i)
    return int(a)+int(b)

print(solution([3, 4, 5, 2, 1]))

