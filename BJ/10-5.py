N = int(input())
i = 0
count = 0
while True:
    i += 1
    if str(i).count('666') >= 1 :
        count += 1
    if count == N:
        print(i)
        break
'''
오답노트
문제를 제대로 안읽음
666이 '연속으로'존재해야함
'''