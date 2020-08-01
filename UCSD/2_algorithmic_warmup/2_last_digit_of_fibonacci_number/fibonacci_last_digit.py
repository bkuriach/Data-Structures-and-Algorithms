# Uses python3
import sys

# def get_fibonacci_last_digit_naive(n):
#     if n <= 1:
#         return n
#
#     previous = 0
#     current  = 1
#
#     for _ in range(n - 1):
#         previous, current = current, previous + current
#
#     return current % 10

def get_fibonacci_last_digit_naive(n):
    fibList = []
    for i in range(n + 1):
        if i == 0:
            fibList.append(0)
        elif i == 1:
            fibList.append(1)
        else:
            fibList.append((fibList[i - 1] + fibList[i - 2])%10)

    return fibList[n] % 10

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))
