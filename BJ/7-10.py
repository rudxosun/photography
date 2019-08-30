N = int(input())
count = 0
for i in range(N):

    S = list(input())
    Spell = []
    Switch = True

    for j in range(len(S)): # 한 단어 내에서

        tmp = S.pop() # 맨 뒤의 스펠링을 뺐다
        #print(Spell)

        if tmp in Spell:  #and Spell[-1] != tmp: # 이미 Spell에 있으면서 바로 앞에 안나왔으면 for문을 다시 시작하자
            #print(tmp)
            if Spell[-1] == tmp:
                pass
            else:
                Switch = False


        Spell.append(tmp)
        tmp = ' '
    if Switch:
        count += 1
print(count)

'''
엄청 오래걸림.
이유? continue와 break 문의 위치 갈피못잡음
for
    if:
    continue
    일 땐 for 문을 다시 시작

'''