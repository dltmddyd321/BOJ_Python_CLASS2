t = int(input())

for i in range(t):
    h,w,n = map(int,input().split())
    #t(테스트케이스)만큼 입력

    #호수 구하기
    line = n//h+1

    #사람 수가 층수로 나누어질때
    if n%h == 0:
        floor = h
        line = n//h
        # //:나누기 연산 후 정수 부분 수만 구함
    else:
        floor=n%h

    result = floor*pow(10,2)+line
    print(result)
