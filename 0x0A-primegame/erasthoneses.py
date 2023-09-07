#!/usr/bin/python3
"""
Function to solve the prime game problem
Using the sieve of eratosthenes
"""


def sieve_of_er(n):
    """
    Function to generate a list of primes upto 'n'

    Args: n(int) - max value

    Returns: list of prime numbers upto n
    """
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False

    p = 2
    while p * p <= n:
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1

    return [i for i, is_prime in enumerate(primes) if is_prime]


def isWinner(x, nums):
    """
    Function to determine winner based on prime values

    Args: x(int) - number of rounds for each player
          nums(int) - an array of n

    Returns: Winners name else returns none
    """
    maria_wins = 0
    ben_wins = 0

    max_n = max(nums)
    primes = sieve_of_er(max_n)

    for n in nums:
        current_player = "Maria"
        numbers = set(range(1, n + 1))
        primes_copy = primes.copy()

        while primes_copy:
            prime = primes_copy.pop(0)
            multiples = set(range(prime, n + 1, prime))
            numbers -= multiples
            if not numbers:
                break

            current_player = "Ben" if current_player == "Maria" else \
                "Maria"

        if current_player == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None
