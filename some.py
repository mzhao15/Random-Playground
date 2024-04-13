def zero_sum(numbers):
    res = []
    tmp = []

    def dfs(res, tmp, numbers, index):
        if len(tmp) > 0 and sum(tmp) == 0:
            res.append(tmp[:])

        for i in numbers[index:]:
            if i != 0:
                tmp.append(i)
                dfs(res, tmp, numbers, index + 1)
                tmp.pop()

    dfs(res, tmp, numbers, 0)

    return res


a = [1, -2, 6, 7, 1]
print(zero_sum(a))
