# 문자열 조작하기
s = 'hello, world!'
s = s.replace('world', 'python')                # world를 python으로
print(s)

# 문자 바꾸기
table = str.maketrans('aeiou', '12345')
print('apple'.translate(table))                   # 'apple'에서 a를 1, e를 2, i를 3, o를 4, u를 5로

# 문자열 분리하기
## split : 기준 문자열로 문자열을 분리
print('apple pear grape pineapple orange'.split())

# 구분자 문자열과 문자열 리스트 연결하기
## join : 구분자 문자열과 문자열 리스트의 요소를 연결하여 문자열로 만듦
print(' '.join(['apple', 'pear', 'grape', 'pineapple', 'orage']))

print('-'.join(['apple', 'pear', 'grape', 'pineapple', 'orage']))

# 소문자를 대문자로 바꾸기
## upper : 모두 대문자로 변경
print('python'.upper())

# 대문자를 소문자로 변경
## lower : 모두 소문자로 변경
print('PYTHON'.lower())

# 왼쪽 공백 삭제
## lstrip
print('         python      '.lstrip())

# 오른쪽 공백 삭제
## rstrip
print('         python      '.rstrip())

# 양쪽 공백 삭제
## strip
print('     python      '.strip())

# 왼쪽 특정 문자 삭제
print(', python.'.lstrip(',.'))

# 오른쪽 특정 문자 삭제
print(', python.'.rstrip(',.'))

# 양쪽 특정 문자 삭제
print(', python.'.strip(',.'))

# 문자열을 왼쪽 정렬하기
print('python'.ljust(10))

# 문자열을 오른쪽 정렬하기
print('python'.rjust(10))

# 문자열을 가운데 정렬하기
print('python'.center(10))

# 메서드 체이닝
print('python'.rjust(10).upper())

# 문자열 왼쪽에 0 채우기
print('35'.zfill(4))
print('3.5'.zfill(6))
print('hello'.zfill(10))

# 문자열 위치 찾기
print('apple pineapple'.find('pl'))