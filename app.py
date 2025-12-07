from functools import lru_cache
from typing import Iterator, List
import argparse

"""
Simple Fibonacci examples.

Save as: C:/Users/Azada Madadi/OneDrive/Desktop/My Projects/app.py
Provides:
 - fib_iter(n): iterative O(n) nth Fibonacci
 - fib_rec(n): recursive with memoization (lru_cache)
 - fib_gen(): infinite generator of Fibonacci numbers
 - fib_list(n): first n Fibonacci numbers as a list

Usage:
    python app.py         # prints first 10 Fibonacci numbers
    python app.py 20      # prints first 20 Fibonacci numbers and the 20th value
    python app.py --mode rec 15
"""



def fib_iter(n: int) -> int:
        """Return the nth Fibonacci number (0-indexed) using iteration."""
        if n < 0:
                raise ValueError("n must be non-negative")
        a, b = 0, 1
        for _ in range(n):
                a, b = b, a + b
        return a


@lru_cache(maxsize=None)
def fib_rec(n: int) -> int:
        """Return the nth Fibonacci number (0-indexed) using recursion with memoization."""
        if n < 0:
                raise ValueError("n must be non-negative")
        if n < 2:
                return n
        return fib_rec(n - 1) + fib_rec(n - 2)


def fib_gen() -> Iterator[int]:
        """Infinite generator of Fibonacci numbers (0, 1, 1, 2, 3, ...)."""
        a, b = 0, 1
        while True:
                yield a
                a, b = b, a + b


def fib_list(n: int) -> List[int]:
        """Return a list of the first n Fibonacci numbers (0-indexed)."""
        if n < 0:
                raise ValueError("n must be non-negative")
        seq = []
        for i, val in zip(range(n), fib_gen()):
                seq.append(val)
        return seq


def main():
        parser = argparse.ArgumentParser(description="Fibonacci examples")
        parser.add_argument("n", nargs="?", type=int, default=10, help="how many Fibonacci numbers to print")
        parser.add_argument("--mode", choices=("iter", "rec"), default="iter", help="which method to use to compute nth value")
        args = parser.parse_args()

        n = args.n
        sequence = fib_list(n)
        print(f"First {n} Fibonacci numbers:")
        print(sequence)

        # compute nth (0-indexed) using chosen mode
        method = fib_iter if args.mode == "iter" else fib_rec
        nth_index = n - 1 if n >= 1 else 0
        print(f"\nUsing {args.mode}: Fibonacci({nth_index}) = {method(nth_index)}")

        # demonstrate generator for first 10 values (or n if smaller)
        print("\nGenerator demo (first min(10,n) values):")
        demo_count = min(10, n)
        g = fib_gen()
        print([next(g) for _ in range(demo_count)])


if __name__ == "__main__":
        main()