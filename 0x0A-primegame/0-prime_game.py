#!/usr/bin/python3
""" Prime Game Module """
from typing import List

players = {
    'Maria': 0,
    'Ben': 0,
}


def prime_factory(n: int) -> List[int]:
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
    return [p for p in range(2, n + 1) if is_prime[p]]


def game_sim(n: int) -> str:
    """
        Simulates the game for a given value of n and returns the winner.

        Args:
            n: integer representing the maximum number in the set

        Returns:
            'Maria' if Maria wins, 'Ben' if Ben wins
    """
    primes = prime_factory(n)
    available_primes = [True] * (n + 1)
    available_primes[0] = available_primes[1] = False
    turn = 'Maria'

    for prime in primes:
        # Ensure the prime is still available
        if available_primes[prime]:
            # print(f'{turn} picks `{prime}`')
            # Mark all multiples of the prime as not available
            for multiple in range(prime, n + 1, prime):
                available_primes[multiple] = False
            # print(f'Available primes after {turn}\'s turn: {available_}')
            if turn == 'Maria':
                turn = 'Ben'
            else:
                turn = 'Maria'
        # Skip to the next prime if the current one is not available
        else:
            continue
    return 'Ben' if turn == 'Maria' else 'Maria'


def isWinner(x: int, nums: List[int]) -> str:
    """
        Determines the player who won the most rounds

        Args:
            x: number of rounds
            nums: list of integers representing n for each round

        Returns:
            Name of the player who won the most rounds, or None if tied
    """
    players = {'Maria': 0, 'Ben': 0}

    for n in nums:
        # print(f"Round: {n}")
        winner = game_sim(n)
        players[winner] += 1
        # print(winner)
        # print()

    if players['Maria'] > players['Ben']:
        return 'Maria'
    elif players['Ben'] > players['Maria']:
        return 'Ben'
    else:
        return None
