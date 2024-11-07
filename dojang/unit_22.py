a = [10, 20, 30]
a.append(500)
print(len(a))

a = []
a.append(10)
print(a)

a = [10, 20, 30]
a.append([500, 600])
print(a)
print(len(a))

a = [10, 20, 30]
a.extend([500, 600])
print(a)
print(len(a))

a = [10, 20, 30]
a.insert(2, 500)
print(a)
print(len(a))

# insert에서 자주 사용하는 패턴 2가지
# insert(0, 요소): 리스트의 맨 처음에 요소를 추가
# insert(len(리스트), 요소): 리스트의 끝에 요소를 추가
a = [10, 20, 30]
a.insert(0, 500)
print(a)

a = [10, 20, 30]
a.insert(len(a), 500)
print(a)

# 리스트 중간에 요소 여러 개 추가
a = [10, 20, 30]
a.insert(1, [500, 600])
print(a)

a[1:1] = [500, 600]
print(a)

# 리스트에서 특정 인덱스의 요소를 삭제하기
## pop() 은 리스트의 마지막 요소를 삭제한 뒤 삭제한 요소 반환
a = [10, 20, 30]
print(a.pop())
print(a)

print(a.pop(1))
print(a)

# 리스트에서 특정 값을 찾아서 삭제하기
a = [10, 20, 30]
a.remove(20)
print(a)

# 리스트에서 특정 값의 인덱스 구하기
## 같은 값이 여러 개일 경우 처음 찾은 인덱스를 구한다
a = [10, 20, 30, 15, 20, 40]
print(a.index(20))

# 특정 값의 개수 구하기
a = [10, 20, 30, 15, 20, 40]
print(a.count(20))

# 리스트의 순서를 뒤집기
a = [10, 20, 30, 15, 20, 40]
a.reverse()
print(a)

# 리스트의 요소를 정렬하기
## 리스트의 요소를 작은 순서대로 정렬(오름차순)
## sort(reverse-True): 리스트의 값을 큰 순서대로 정렬(내림차순)
a = [10, 20, 30, 15, 20, 40]
a.sort()
print(a)

# 리스트의 모든 요소를 삭제하기
a = [10, 20, 30]
a.clear()
print(a)

a = [10, 20, 30]
del a[:]
print(a)

# 리스트를 슬라이스로 조작하기
## 리스트 씉에 값이 한 개 들어있는 리스트 추가
a = [10, 20, 30]
a[len(a):] = [500]
print(a)

# 리스트를 다른 변수에 할당하기
a = [0, 0, 0, 0, 0]
b = a
# 리스트 b의 요소를 변경하면 리스트 a와 b에 모두 반영
b[2] = 99
print(a)
print(b)


a = [0, 0, 0, 0, 0]
b = a.copy()
print(a)
print(b)

# 반복문으로 요소 출력하기
a = [38, 21, 53, 62, 19]
for i in a:
    print(i)

# 인덱스와 요소를 함께 출력하기
a = [38, 21, 53, 62, 19]
for index, value in enumerate(a):
    print(index, value)

# 1부터 출력하고 싶은 경우
a = [38, 21, 53, 62, 19]
for index, value in enumerate(a):
    print(index + 1, value)

# 좀 더 파이썬 다운 방법
for index, value in enumerate(a, start=1):
    print(index, value)

# while 반복문으로 요소 출력하기
a = [38, 21, 53, 62, 19]
i = 0
while i < len(a):
    print(a[i])
    i += 1                    # i가 1씩 증가하도록

# 가장 작은 수와 가장 큰 수 구하기
a = [38, 21, 53, 62, 19]
smallest = a[0]
for i in a:
    if i < smallest:
        smallest = i
print(i)

a = [38, 21, 53, 62, 19]
largest = a[0]
for i in a:
    if i > largest:
        largest = i
print(i)

# sort : 리스트 정렬
a = [38, 21, 53, 62, 19]
# a.sort()
a.sort(reverse=True)
print(a[0])

a = [38, 21, 53, 62, 19]
# print(min(a))
print(max(a))

# 요소의 합계 구하기
a = [10, 10, 10, 10, 10]
# x = 0
# for i in a:
#     x += i
# print(x)
print(sum(a))

# 리스트 표현식 사용하기
a = [i for i in range(10)]                  # 0부터 9까지 숫자를 생성하여 리스트 생성
print(a)
b = list(i for i in range(10))
print(b)

c = [i + 5 for i in range(10)]                # 0부터 9까지 숫자를 생성하면서 값에 5를 더하여 리스트 생성
print(c)

d = [i * 2 for i in range(10)]                # 0부터 9까지 숫자를 생성하면서 값에 2를 곱하여 리스트 생성
print(d)

# 리스트 표현식에서 if 조건문 사용하기
a = [i for i in range(10) if i % 2 == 0]        # 0~9 숫자 중 2의 배수인 짝수로 리스트 생성
print(a)

b = [i + 5 for i in range(10) if i % 2 == 1]      # 0~9 숫자 중 홀수에 5를 더하여 리스트 생성
print(b)

# for 반복문과 if 조건문을 여러 번 사용하기
a = [i * j for j in range(2, 5) for i in range(1, 10)]      # 2단부터 4단까지 구구단 리스트 생성
a = [i * j for j in range(2, 5)
            for i in range(1, 10)]
print(a)

# 리스트에 map 사용하기
## map: 리스트의 요소를 지정된 함수로 처리해주는 함수
a = [1.2, 2.5, 3.7, 4.6]        # 리스트의 모든 요소를 정수로 변환
for i in range(len(a)):
    a[i] = int(a[i])
print(a)

a = [1.2, 2.5, 3.7, 4.6]
a= list(map(int, a))
print(a)

# map 모든 반복 가능한 객체 사용 가능
a= list(map(str, range(10)))            # str : 모두 문자열로 변환
print(a)

a = map(int, input().split())
print(list(a))

## 튜플에서 특정 값의 인덱스 구하기
a = (38, 21, 53, 62, 19, 53)
# print(a.index(53))
print(a.count(20))

## for 반복문으로 요소 출력하기
a = (38, 21, 53, 62, 19)
for i in a:
    print(i, end=' ')

# 튜플 표현식 사용하기
a = tuple(i for i in range(10) if i % 2 == 0)
print(a)

# tuple에 map 사용하기
a = (1.2, 2.5, 3.7, 4.6)
a = tuple(map(int, a))
print(a)

# 튜플에서 가장 작은 수, 가장 큰 수, 합계 구하기
a = (38, 21, 53, 62, 19)
print(min(a))
print(max(a))
print(sum(a))