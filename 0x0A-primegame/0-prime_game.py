#!/usr/bin/python3
"""Function to solve the Prime Game problem"""


def is_prime(n):
    """Check if n is a prime number"""
    for i in range(2, int(n ** 0.5) + 1):
        if not n % i:
            return False
    return True


def add_prime(n, primes):
    """Add prime to the list"""
    last_prime = primes[-1]
    if n > last_prime:
        for i in range(last_prime + 1, n + 1):
            if is_prime(i):
                primes.append(i)
            else:
                primes.append(0)


def isWinner(x, nums):
    """Determine the name of the player that won the most rounds

    Args:
        x (int): Number of rounds
        nums (list): Array of n

    Returns:
        str: Name of the player that won the most rounds.
             If the winner cannot be determined, returns None.
    """
    score = {"Maria": 0, "Ben": 0}
    primes = [0, 0, 2]
    add_prime(max(nums), primes)

    for r in range(x):
        _sum = sum((i != 0 and i <= nums[r])
                   for i in primes[:nums[r] + 1])
        if _sum % 2:
            winner = "Maria"
        else:
            winner = "Ben"
        if winner:
            score[winner] += 1

    if score["Maria"] > score["Ben"]:
        return "Maria"
    elif score["Ben"] > score["Maria"]:
        return "Ben"

    return None
