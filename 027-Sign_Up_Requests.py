# 入力
N = int(input()) 

user_name = []
for _ in range(N):
    user_name.append(input())

index = {}

# 出力
for i in range(N):
    if user_name[i] not in index:
        index[user_name[i]] = 1
        print(i+1)
