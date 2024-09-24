def solution(num_list):
    n1 = num_list[-1]
    n2 = num_list[-2]
    answer = num_list
    if n1 > n2:
        answer.append(n1 - n2)
    else:
        answer.append(n1 * 2)
    return answer



# def solution(l):
#     l.append(l[-1]-l[-2] if l[-1]>l[-2] else l[-1]*2)
#     return l

print(solution([2, 1, 6]))