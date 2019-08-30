N = int(input())
N_list = []
for i in range(N):
    a, b = input().split()
    info = (int(a), b, i)
    N_list.append(info)
Result = sorted(N_list, key=lambda info : (info[0], info[2]))
for i in range(N):
    print(Result[i][0], Result[i][1])


"""
s = sorted(s, key = lambda x: (x[1], x[2]))

a = [('Al', 2),('Bill', 1),('Carol', 2), ('Abel', 3), ('Zeke', 2), ('Chris', 1)]  
b = sorted(sorted(a, key = lambda x : x[0]), key = lambda x : x[1], reverse = True)  
print(b)  
[('Abel', 3), ('Al', 2), ('Carol', 2), ('Zeke', 2), ('Bill', 1), ('Chris', 1)]
의 차이점은?
같은 결과 그러나

1번 방식이 파이써닉함
우선순위를 x1먼저, x2를 나중에 두기까지 함
"""

"""
오딥노트
a 에 int 안뭍여서 숫자정렬로 안되었었음
"""