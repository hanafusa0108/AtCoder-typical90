import sys

def main():
    # 入力
    H, W = map(int, input().split())

    # 辺が1以下の時
    if H == 1 or W == 1:
        print(H * W)
        sys.exit()

    # 出力
    print(((H + 1) // 2) * ((W + 1) // 2))

if __name__ == '__main__':
    main() 