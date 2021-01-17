from math import sqrt

def isPrime(n):
    if n <= 1:
        return False
    if n == 2:
        return True

    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def getPrimes(n):
    primes = ""
    i = 0
    while len(primes) < n:
        if isPrime(i):
            primes += str(i)
        i = i + 1
    return primes


def solution(n):
    result = getPrimes(n + 5)
    return result[n: n+5]


