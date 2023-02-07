K = int(input())
lenth = [(input().split()) for _ in range(6)]
# lenth_int = list(map(int,(lenth)))
# print(lenth)

x = []
y = []

for idx in lenth:
    if int(idx[0]) == 4 or int(idx[0]) == 3:
        x.append(int(idx[1]))
    if int(idx[0]) == 1 or int(idx[0]) == 2:
        y.append(int(idx[1]))
print(x, y)
area = max(x)*max(y)







    