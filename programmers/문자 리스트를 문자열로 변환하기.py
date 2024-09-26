def solution(arr):
    answer = ''
    i = arr
    for i in range(len(arr)):
        answer += arr[i]        
    return answer

print(solution(["a","b","c"]))