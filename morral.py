def fill_bag(max_weight, weight, profit, n):
    if n==0 or max_weight ==0:
        return 0
    if weight[n-1] > max_weight:
        return fill_bag(max_weight, weight, profit, n - 1)
    return max(
            profit[n-1] + fill_bag(max_weight - weight[n-1], weight, profit, n-1),
            fill_bag(max_weight, weight, profit, n-1)
            )


if __name__ == '__main__':
    profit = [60, 100, 120]
    weight = [10, 20, 30]
    max_weight = 60
    n = len(profit)

    result = fill_bag(max_weight, weight, profit, n)
    print(result)
