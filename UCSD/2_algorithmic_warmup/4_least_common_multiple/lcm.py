# Uses python3
import sys

def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a*b

def gcd_euclidean(a, b):
    if b == 0:
        return a
    aPrime = a%b

    return gcd_euclidean(b, aPrime)

def lcm_fast(a, b):
    product = a*b

    lcm = int(product/gcd_euclidean(a,b))

    return lcm

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    # print(lcm_naive(a, b))
    print(lcm_fast(a, b))
