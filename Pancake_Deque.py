def lis(sequence, len_list):
    maximum = -1
    cur_len = 0
    for i in range(len(sequence)):
        if sequence[i] >= maximum:
            maximum = sequence[i]
            cur_len += 1
        len_list.append(cur_len)

T = int(input())

for index, t in enumerate(range(T)):
    left_lis_len, right_lis_len = [], []
    left_max, right_max = -1, -1

    N = int(input())
    D = [int(d) for d in input().split(" ")]
    lis(D[:-1], left_lis_len)
    D.reverse()
    lis(D[:-1], right_lis_len)
    maximum = -1
    for i in range(len(D) - 1):
        maximum = max(left_lis_len[i] + right_lis_len[-1 - i], maximum)

    print(f"Case #{index+1}: {maximum}")

