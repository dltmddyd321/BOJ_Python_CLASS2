N, M = map(int, input().split())
card = list(map(int,input().split()))

result = 0

for i in range(N):
    for j in range(i+1, N): #i 한 장 뽑았으므로 i+1부터~
        for k in range(j+1, N):
            if card[i]+card[j]+card[k] > M :
                continue #아래의 코드를 실행하지 않는다.
            else:
                result = max(result,card[i]+card[j]+card[k])
print(result)
