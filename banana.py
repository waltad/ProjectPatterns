import itertools


def bananas(s):
    result = set()

    for comb in itertools.combinations(range(len(s)), len(s) - 6):
        arr = list(s)

        for i in comb:
            arr[i] = '-'

        candidate = ''.join(arr)

        if candidate.replace('-', '') == 'banana':
            result.add(candidate)

    return result


def banana2(s):
    n_lst = [_ for _ in range(len(s))]
    ch_lst = [ch for ch in s]
    r = len(s) - 6
    output = []
    for x in itertools.combinations(n_lst, r):
        copy_ch = ch_lst.copy()
        for i in x:
            copy_ch[i] = '-'
        if "".join(copy_ch).replace('-', '') == 'banana':
            output.append("".join(copy_ch))
    return output


if __name__ == '__main__':
    x = "bbananana"
    print(bananas(x))
    print(banana2(x))
