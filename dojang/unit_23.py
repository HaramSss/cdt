# 2차원 리스트를 만들고 요소에 접근하기
a = [[10, 20], [30, 40], [50, 60]]
a = [[10, 20],
     [30, 40],
     [50, 60]]
print(a)


# 2차원 리스트의 요소에 접근하기
a = [[10, 20], [30, 40], [50, 60]]
print(a[0][0])                          # 세로 인덱스 0, 가로 인덱스 1인 요소 출력
print(a[2][1])                          # 세로 인덱스 1, 가로 인덱스 1인 요소 출력

a[0][1] = 1000                          # 세로 인덱스 0, 가로 인덱스 1인 요소에 값 할당
print(a[0][1])

# for 반복문을 한 번만 사용하기
a = [[10, 20], [30, 40], [50, 60]]
for x, y in a:                              # 리스트의 가로 한 줄(안쪽 리스트)에서 요소 두 개를 꺼냄
    print(x, y)

# for 반복문을 두 번 사용하기
a = [[10, 20], [30, 40], [50, 60]]

for i in a:                             # a에서 안쪽 리스트를 꺼냄
    for j in i:                         # 안쪽 리스트에서 요소를 하나씩 꺼냄
        print(j, end=' ')
    print()

# for와 range 사용하기
a = [[10, 20], [30, 40], [50, 60]]
for i in range(len(a)):                 # 세로 크기 3만큼 반복
    for j in range(len(a[i])):          # 가로 크기 2만큼 반복
        print(a[i][j], end=' ')
    print()

# while 반복문을 한 번 사용하기
a = [[10, 20], [30, 40], [50, 60]]
i = 0
while i < len(a):                   # 반복할 때 리스트의 크기 활용(세로 크기)
    x, y = a[i]                     # 요소 두 개를 한꺼번에 가져오기
    print(x, y)
    i += 1                          # 인덱스를 1 증가시킴

# while 반복문을 두 번 사용하기
a = [[10, 20], [30, 40], [50, 60]]
i = 0
while i < len(a):                   # 세로 크기
    j = 0
    while j < len(a[i]):            # 가로 크기
        print(a[i][j], end=' ')
        j += 1                      # 가로 인덱스를 1 증가
    print()
    i += 1                          # 세로 인덱스를 1 증가

# for 반복문으로 1차원 리스트 만들기
a = []                                # 빈 리스트 생성
for i in range(10):
    a.append(0)                       # append로 요소 추가
print(a)

# for 반복문으로 2차원 리스트 만들기
a = []                                  # 빈 리스트 생성
for i in range(3):
    line = []                           # 안쪽 리스트로 사용할 빈 리스트 생성
    for j in range(2):
        line.append(0)                  # 안쪽 리스트에 0 추가
        a.append(line)                  # 전체 리스트에 안쪽 리스트를 추가
print(a)

# 리스트 표현식으로 2차원 리스트 만들기
a = [[0 for j in range(2)] for i in range(3)]
print(a)

# 톱니형 리스트 만들기
a = [3, 1, 3, 2, 5]                     # 가로 크기를 저장한 리스트
b = []

for i in a:
    line = []                           # 가로 크기를 저장한 리스트로 반복
    for j in range(i):                  # 안쪽 리스트로 사용할 빈 리스트 생성
        line.append(0)                  # 리스트 a에 저장된 가로 크기만큼 반복
    b.append(line)              
print(b)                                # 리스트 b에 안쪽 리스트를 추가

