n = int(input())
w_list = []

for i in range(n) :
    w_list.append(input())

set_word = list(set(w_list))
#중복 제거를 통해 정렬

sort_word = []
for i in set_word:
    sort_word.append((len(i),i))
    #리스트 속 단어들을 길이와 단어로 묶어 정렬.
    #단어 길이순으로 관리하기 간편해진다.

result = sorted(sort_word)

for len_word, w_list in result:
    print(w_list)
