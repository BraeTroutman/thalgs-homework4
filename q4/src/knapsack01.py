import sys
import re

filename = sys.argv[1]

f = open(filename, "r")
lines = f.read().split("\n")[:-1]
f.close()

W = int(re.search(r"\d+", lines[0]).group(0))

wtsvals = [list(map(int,re.findall(r"\d+", line))) for line in lines[2:]]
wt = [x[0] for x in wtsvals]
vl = [x[1] for x in wtsvals]

def knapsack(vals: list[int], weights: list[int], cap: int) -> list[list[int]]:
    n = len(vals)

    dp = [[0 for j in range(cap+1)] for i in range(n+1)]

    for i in range(n+1):
        for j in range(cap+1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif weights[i-1] <= j:
                dp[i][j] = max(dp[i-1][j-weights[i-1]] + vals[i-1], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]

    return dp[n][cap]

def constantSpaceKnapsack(vals: list[int], weights: list[int], cap: [int]) -> int:
    n = len(vals)
    prev = [0 for j in range(cap+1)]
    curr = [0 for j in range(cap+1)]

    for i in range(1,n+1):
        for j in range(cap+1):
            if j == 0:
                curr[j] = 0
            elif weights[i-1] <= j:
                curr[j] = max(prev[j-weights[i-1]] + vals[i-1], prev[j])
            else:
                curr[j] = prev[j]
        prev = [x for x in curr]

    return curr[-1]

def showTable(tbl: list[list[int]]):
    n = len(tbl)
    m = len(tbl[0])

    for i in range(n):
        for j in range(m):
            print(tbl[i][j], end="\t")
        print()

print("2D solution")
print(knapsack(vl, wt, W))
print("Space Efficient Solution")
print(constantSpaceKnapsack(vl, wt, W))
