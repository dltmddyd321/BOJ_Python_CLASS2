n = int(input())
mem_list = []

for i in range(n):
    age, name = map(str,input().split())
    age = int(age)
    mem_list.append((age, name))

mem_list.sort(key = lambda x : x[0])
#list에서 [0] 위치인 age만을 key값으로 하여 비교한다.

for i in mem_list:
    print(i[0], i[1])
