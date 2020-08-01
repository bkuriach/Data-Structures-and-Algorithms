# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next  = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

    return sum % 10

def pisano_period(m):
    previous, current = 0, 1
    for i in range(0, m * m):
        previous, current = current, (previous + current) % m
        # A Pisano Period starts with 01
        if (previous == 0 and current == 1):
            return i + 1


def fibonacci_partial_sum_fast(from_, to):

    def fib(n):
        period = pisano_period(10)
        n = n % period
        fibList = []
        sum = 0
        for i in range(n + 1):
            if i == 0:
                fibList.append(0)
            elif i == 1:
                fibList.append(1)
            else:
                fibList.append((fibList[i - 1] + fibList[i - 2]))

            sum += fibList[i]
        return sum%60

    if from_ ==0:
        fromFib = fib(from_)
    else:
        fromFib = fib(from_-1)
    totalFib = fib(to)

    if totalFib > fromFib:
        return (totalFib - fromFib)%10
    else:
        return (fromFib - totalFib)%10

def fib(n):
    # The first two Fibonacci numbers
    f0 = 0
    f1 = 1

    # Base case
    if (n == 0):
        return 0
    if (n == 1):
        return 1
    else:

        # Pisano Period for % 10 is 60
        rem = n % 60

        # Checking the remainder
        if (rem == 0):
            return 0

        # The loop will range from 2 to
        # two terms after the remainder
        for i in range(2, rem + 3):
            f = (f0 + f1) % 60
            f0 = f1
            f1 = f

        s = f1 - 1
        return (s)

def fib_cal(from_,to):
    final = fib(to) - fib(from_ - 1)

    return final %10


if __name__ == '__main__':
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fib_cal(from_, to))