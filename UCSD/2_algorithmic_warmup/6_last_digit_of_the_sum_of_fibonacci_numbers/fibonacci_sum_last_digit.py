# Uses python3
import sys

def fibonacci_sum_naive(n):
    if n <= 1:
        return n
    previous = 0
    current  = 1
    sum      = 1
    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current
    return sum % 10

def pisano_period(m):
    previous, current = 0, 1
    for i in range(0, m * m):
        previous, current \
            = current, (previous + current) % m

        # A Pisano Period starts with 01
        if (previous == 0 and current == 1):
            return i + 1

def fibonacci_sum_fast(n):
    period = pisano_period(10)
    n = n % period
    # print(period, n)
    fibList = []
    sum = 0
    for i in range(n + 1):
        if i == 0:
            fibList.append(0)
            sum += fibList[i]
        elif i == 1:
            fibList.append(1)
            sum += fibList[i]
        else:
            fibList.append((fibList[i - 1] + fibList[i - 2]))
            sum += fibList[i]
    # print(fibList)
    return (sum) % 10

# http://thisthread.blogspot.com/2018/02/last-digit-of-sum-of-fibonacci-numbers.html
def solution(number):
    if number < 2:
        return number

    number %= 60

    results = [1, 1]
    for _ in range(number):  # 2
        results.append((results[-1] + results[-2]) % 10)  # 3
    print(results)
    return (results[-1] - 1) % 10  # 4

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_fast(n))


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