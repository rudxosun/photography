Num_Student = int(input())
P_list = []
for i in range(Num_Student):
    Scores = list(map(int, input().split()))
    print(Scores)
    Mean_Scores = sum(Scores[1:])/(Scores[0])
    Over_Scores = [Score for Score in Scores if Score > Mean_Scores]
    Posivility = ((len(Over_Scores)/(len(Scores)-1))*100)
    print("%.3f%%" % round(Posivility, 3))
    #P_list.append(Posivility)
    #if len(P_list) == int(Num_Student):
#for j in range(len(P_list)):
#    print("%.3f%%" % round(P_list[j], 3))
'''

# 왜 인풋이 들어가고 엔터(리턴)를 하기 전에 결과값이 나오는 걸까?
# For 문이라서?
# for문 안에 print가 있어서 바로 됨 -> 리스트 생성 후 for 문 밖에서 print out 하자
# 해결! 인 줄 알았찌만
# 한 for 문에 없다면 input해주고 바로 작동 안됨 -> 조건문 걸어서 

# 소숫점 3째자리까지 강제로(10%면 10.000%까지)하는 법
# print("%.3f" %숫자)

왜 for 문에 print가 있으면 엔터하기 전까진 n-1번째까지 진행이 되다가 n번째는 엔터 후에 진행이 되는거지?
'''
'''
5
5 50 50 70 80 100
7 100 95 90 80 70 60 50
3 70 90 80
3 70 90 81
9 100 99 98 97 96 95 94 93 91
'''