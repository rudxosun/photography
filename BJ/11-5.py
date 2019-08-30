N_list = list(input())
New_list = []
for i in range(len(N_list)):
    New_list.append(int(N_list[i]))
New_list.sort(reverse=True)
X = ""
for i in range(len(New_list)):
    X = X + str(New_list[i])
print(X)