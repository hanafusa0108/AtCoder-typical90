def main():
    #入力の読み込み
    H, W = map(int,input().split()) 
    A = [list(map(int, input().split())) for l in range(H)]

    #前処理

    #横の和
    width = list(map(sum, A))

    #縦の和
    length = list(map(sum, zip(*A)))

    #結果を出力
    for i in range(H):
        result = []
        for j in range(W):
            result.append(width[i] + length[j] - A[i][j])
        
        print(*result)

if __name__ == '__main__':
    main()