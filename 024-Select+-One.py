import sys
# 入力
N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 増減の回数
diff = 0
for i in range(N):
    diff += abs(B[i] - A[i])

counter = K - diff

# 出力
if counter < 0:
    print("No")
    sys.exit()

if counter % 2 != 0:
    print("No")
    sys.exit()

print("Yes")
    