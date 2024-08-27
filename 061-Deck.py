def main():
    # 入力
    Q = int(input())
    tx = [map(int, input().split()) for _ in range(Q)]
    t, x = [list(i) for i in zip(*tx)]

    # 出力
    card = []
    for i in range(Q):
        if t[i] == 1:
            card.insert(0, x[i])
        
        elif t[i] == 2:
            card.append(x[i])

        else:
            print(card[x[i]-1])

if __name__ == '__main__':
    main()