#!/usr/bin/python3
""" Prime Game Module """

players = {
    'Maria': 0,
    'Ben': 0,
}


def prime_factory(n: int) -> list[int]:
    """
        Returns a list of all prime numbers up to n

        Args:
            n - integer limit of prime list

        Returns:
            List of prime numbers up to `n`
    """
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    p = 2

    while p * p <= n:
        if is_prime[p]:
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    return is_prime


def isWinner(x: int, nums: list[int]) -> str:
    """
        Determines the player who won the most rounds

        Args:
            x: number of rounds
            nums: list of integers representing n for each round

        Returns:
            Name of the player who won the most rounds, or None if tied
    """
    if x < 1 or not nums:
        return None
    max_n = max(nums)
    primes = prime_factory(max_n)
    maria_wins, ben_wins = 0, 0

    for n in nums:
        primes_count = sum(primes[:n + 1])
        if primes_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins < maria_wins:
        return 'Ben'
    else:
        return None
