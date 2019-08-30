N = int(input())
Weight = []
for i in range(N):
    Weight.append(list(map(int, input().split())))
#[[x1,y1],[x2,y2]]
for i in range(N):
    over = 0
    for j in range(N):
        if Weight[i][0] < Weight[j][0] and Weight[i][1] < Weight[j][1]:
            over += 1
    print(over+1)
