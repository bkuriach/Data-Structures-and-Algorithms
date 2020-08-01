# Uses python3
# def calc_fib(n):
#     if (n <= 1):
#         return n
#     return calc_fib(n - 1) + calc_fib(n - 2)

def calc_fib(n):
    fibList = []
    for i in range(n+1):
        if i == 0:
            fibList.append(0)
        elif i == 1:
            fibList.append(1)
        else:
            fibList.append(fibList[i-1]+fibList[i-2])
    return fibList[n]

n = int(input())
print(calc_fib(n))

