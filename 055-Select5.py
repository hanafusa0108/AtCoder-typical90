import itertools

def main():
    #入力
    N, P, Q = map(int, input().split())

    A = list(map(int, input().split()))
    A.sort()

    # 事前に余りを求めておく
    for i in range(N):
        A[i] = A[i] % P

    cnt = 0

    # 全探索
    for i in range(N):
        for j in range(i):
            for k in range(j):
                for l in range(k):
                    for m in range(l):
                        if (A[i] * A[j] * A[k] * A[l] * A[m]) % P == Q:
                            cnt += 1

    # 出力
    print(cnt)

if __name__ == '__main__':
    main() 
