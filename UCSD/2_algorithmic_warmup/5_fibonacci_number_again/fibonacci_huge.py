# Uses python3
import sys

# def get_fibonacci_huge_naive(n, m):
#     if n <= 1:
#         return n
#
#     previous = 0
#     current  = 1
#
#     for _ in range(n - 1):
#         previous, current = current, previous + current
#
#     return current % m


def pisano_period(m):
    previous, current = 0, 1
    for i in range(0, m * m):
        previous, current \
            = current, (previous + current) % m

        # A Pisano Period starts with 01
        if (previous == 0 and current == 1):
            return i + 1

def fibonacci_modulo_m(n, m):

    period = pisano_period(m)
    n = n % period
    # print(period, n)
    fibList = []
    for i in range(n + 1):
        if i == 0:
            fibList.append(0)
        elif i == 1:
            fibList.append(1)
        else:
            fibList.append((fibList[i - 1] + fibList[i - 2]))
    # print(fibList)
    return fibList[n] % m


if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(fibonacci_modulo_m(n, m))
