N = int(input())
Scores = list(map(int,input().split()))
NewScores = [100*Scores[j]/max(Scores) for j in range(N)]
print(sum(NewScores)/N)