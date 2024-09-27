def solution(my_strings, parts):
    answer = ''
    for i in range(len(my_strings)):
        a = my_strings[i] #progressive
        b = parts[i] #[0,4]
        c = a[b[0]:b[1]+1]
        answer += c
    return answer


print(solution(["progressive", "hamburger", "hammer", "ahocorasick"], [[0, 4], [1, 2], [3, 5], [7, 7]]))