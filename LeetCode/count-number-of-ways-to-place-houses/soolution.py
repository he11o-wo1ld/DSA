def countHousePlacements(n):
        return fib(n + 1) ** 2 % (10 ** 9 + 7)
    
def fib(n):
    a, b, c, d, mod = 1, 1, 0, 1, 10 ** 9 + 7
    while n:
        if n & 1:
            a, b = a * c + b * d, a * d + b * c + b * d
            n -= 1
        else:
            c, d = c * c + d * d, 2 * c * d + d * d
            n >>= 1
        a, b, c, d = a % mod, b % mod, c % mod, d % mod
    return a

print(countHousePlacements(1))
