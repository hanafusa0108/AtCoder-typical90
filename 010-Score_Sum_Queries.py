# 入力の読み込み
N = int(input())
cp = [map(int, input().split()) for _ in range(N)]
C, P = [list(i) for i in zip(*cp)]

Q = int(input())
lr = [map(int, input().split()) for _ in range(Q)]
L, R = [list(i) for i in zip(*lr)]

# 添字を1から使えるようにする
C = [0] + C
P = [0] + P
L = [0] + L
R = [0] + R

sum1 = [0] * (N+1)
sum2 = [0] * (N+1)

# 累積和を求める
for i in range(1,N+1):
    sum1[i] = sum1[i-1]
    sum2[i] = sum2[i-1]

    if C[i] == 1:
        sum1[i] += P[i]
    
    if C[i] == 2:
        sum2[i] += P[i]
    
# 出力
for i in range(1, Q+1):
    class1 = sum1[R[i]] - sum1[L[i] - 1]
    class2 = sum2[R[i]] - sum2[L[i] - 1]
    print(class1, class2)
