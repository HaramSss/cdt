def solution(num_list):
    answer = 0
    a = 0
    b = 0
    for i in range(len(num_list)):
        if i % 2 == 0:
            a += num_list[i] # list 안의 수
        else:
            b += num_list[i]
    if a >= b:
        return a
    else:
        return b
    

print(solution([4, 2, 6, 1, 7, 6]))
    

# def solution(num_list):
#     return max(sum(num_list[::2]), sum(num_list[1::2]))

