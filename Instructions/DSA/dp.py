dp = r'''
## Dynamic Programming
Dynamic Programming (DP) is a powerful optimization technique used to solve problems that exhibit overlapping subproblems and optimal substructure. It involves solving problems by breaking them into smaller subproblems, solving each subproblem once, and storing their results for reuse.

Here's a detailed explanation with Python examples:

Key Concepts
- Overlapping Subproblems: The problem can be divided into subproblems, which are reused multiple times.
- Optimal Substructure: The solution to a problem can be constructed from solutions to its subproblems.
- Memoization (Top-Down): Storing the results of subproblems to avoid redundant computations.
- Tabulation (Bottom-Up): Iteratively solving and storing the results of subproblems in a table.


```python
# Dynamic Programming in Python

"""
## Example 1: Fibonacci Numbers using DP
The Fibonacci sequence is a classic example of overlapping subproblems.
"""

# Fibonacci using Memoization (Top-Down)
def fib_memoization(n, memo={}):
    if n <= 1:
        return n
    if n not in memo:
        memo[n] = fib_memoization(n - 1, memo) + fib_memoization(n - 2, memo)
    return memo[n]

# Fibonacci using Tabulation (Bottom-Up)
def fib_tabulation(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

"""
## Example 2: 0/1 Knapsack Problem
Given weights and values of items, find the maximum value that can be obtained for a given capacity.
"""

# 0/1 Knapsack using Tabulation
def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
            else:
                dp[i][w] = dp[i - 1][w]
    
    return dp[n][capacity]

"""
## Example 3: Longest Common Subsequence (LCS)
Given two strings, find the length of their longest common subsequence.
"""

# Longest Common Subsequence using Tabulation
def lcs(X, Y):
    m, n = len(X), len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[m][n]

```
### Summary:
- Use **Memoization** for recursive problems where subproblems are solved multiple times.
- Use **Tabulation** for iterative approaches where we solve subproblems in a bottom-up manner.
- Dynamic Programming is applicable when the problem exhibits overlapping subproblems and optimal substructure.


'''
