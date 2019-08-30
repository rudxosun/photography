P = []
for i in range(3):
    P.append(list(map(int, input().split())))

#[[x1,y1],[x2,y2],[x3,y3]]
X = [P[i][0] for i in range(3)]
Result_X =[ P[i][0] for i in range(3)]
Y = [P[i][1] for i in range(3)]
Result_Y = [P[i][1] for i in range(3)]

for i in range(3):
    for j in range(3):
        if P[i][0] == P[j][0] and i != j: #X값이 같으면 그 값은 네 번째 점의 좌표가 아님
            Result_X.remove(P[i][0])
        if P[i][1] == P[j][1] and i != j:
            Result_Y.remove(P[i][1])
print(Result_X[0], Result_Y[0])
