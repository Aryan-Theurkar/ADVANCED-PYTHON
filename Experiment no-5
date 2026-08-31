def fibonacci(n, memo=None):
    if memo is None:
        memo = {}
        
    if n <= 1:
        return n
    if n in memo:
        return memo[n]
        
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]

n = 10
for i in range(n):
    print(fibonacci(i), end=" ")
