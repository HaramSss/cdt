# a, b = map(int, input().split(' '))
# print(f"a = {a}")
# print(f"b = {b}")

# mx=[[100, 101, 102], [103, 104, 105], [106, 107, 108]]
# for i in range(len(mx)):
# 	for j in range(len(mx[i])):
# 		print(i, "행", j, "열:", mx[i][j], end="")
# 	print()
	
count=1
while True:
    print("*")
    if count>=10:
        break
    count+=1

count=0
while count<=10:
    count+=1
    if count%2==0:
        continue
    print(count)