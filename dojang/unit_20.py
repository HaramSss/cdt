for i in range(10):
    print(i)

for i in range(10):
    if i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)

for i in range(1, 10):
    if i % 3 == 0 and i % 5 == 0:
        print('fizzbuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)

# i가 30인데 if에서 3의 배수를 먼저 검사하면 3과 5의 공배수는 검사하지 않고 넘어감
# 따라서 3과 5의 공배수를 먼저 검사한 뒤 elif로 3의 배수, 5의 배수를 검사해야 한다.


## 논리 연산자를 사용하지 않고 3과 5의 공배수 처리하기
for i in range(1, 10):
    if i % 15 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)

### 코드 단축하기
for i in range(1, 10):
    print('Fizz' * (i % 3 == 0) + 'Buzz' * (i % 5 == 0) or i)
# 문자열 곱셈과 덧셈을 이용하여 print 안에서 처리
