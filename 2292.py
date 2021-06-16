n = int(input())

num_step = 1 #벌집 개수, 1개로 초기화

cnt = 1

while n > num_step :
    num_step += 6*cnt #벌집이 6의 배수로 증가
    cnt += 1
print(cnt)
