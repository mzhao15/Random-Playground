
def backtrack(coins, target, start):
    if target == 0:
        return 1
    elif target < 0:
        return 0
    
    cur_sum = 0
    for i in range(start, len(coins)):
        cur_sum += backtrack(coins, target - coins[i], start)
    
    return cur_sum

coins = [1, 2, 3]
target = 4
coins.sort()
print(backtrack(coins, target, 0))