i = 0
while i < 10:
    print('hello, world')
    i += 1

i = 1
while i <= 10:
    print('hello, world', i)
    i += 1

i = 10
while i > 0:
    print('hello, world', i)
    i -= 1

count = int(input('반복할 횟수를 입력하세요: '))

i = 0
while i < count:
    print('hello, world', i)
    i += 1

while count > 0 :
    print('hello, world', count)
    count -= 1

import random

i = 0
while i != 3:                       # 1과 6사이의 난수를 생성한 뒤 3이 나오면 반복을 끝낸다.
    i = random.randint(1, 6)        # randint : 1과 6 사이의 난수를 생성
    print(i)

while True:                           # while에 True를 지정하면 무한 루프
    print('hello, world')

while 1:                              # 0이 아닌 숫자는 True 로 취급하여 무한 루프로 동작
    print('hello, world')

while 'hello':                        # 내용이 있는 문자열은 True로 취급하여 무한 루프로 동작
    print('hello, world') 