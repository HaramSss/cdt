def solution(str_list, ex):
    answer = ''
    for i in str_list:
        if ex not in i:
            answer += i
    return answer

print(solution(["abc", "def", "ghi"], "ef"))


# def solution(str_list, ex):
#     return ''.join([i for i in str_list if ex not in i])