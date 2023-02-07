N = int(input())
num = (input().split())
print(N)
# print(num)
num_lst = []
for i in num:
    num_lst.append(int(i))
print(num_lst)

cnt = 0
for i in range(len(num_lst)):
    if num_lst[i] <= num_lst[i+1]:
        cnt +=1
    else:
        pass
print(cnt)

