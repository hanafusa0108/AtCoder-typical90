import numpy as np

def main():
    N, K = map(int, input().split())
    octal_num = str(N)

    for _ in range(K):
        # 8進数から10進数
        decimal_num = int(octal_num, 8)

        # 10進数から9進数
        octal_num = np.base_repr(decimal_num, 9)
        octal_num = str(octal_num)

        # 文字列をリストに変換
        octal_num_list = list(octal_num)

        for i in range(len(octal_num_list)):
            if octal_num_list[i] == '8':
                octal_num_list[i] = '5'
        
        # リストを再び文字列に変換
        octal_num = ''.join(octal_num_list)

    print(octal_num)

if __name__ == '__main__':
    main()