# Uses python3
import sys

# def get_change(m):
#     coinCount = 0
#     while m > 0:
#         if m >= 10:
#             m = m-10
#             coinCount +=1
#         elif m >= 5:
#             m = m-5
#             coinCount += 1
#         elif m >= 1:
#             m = m-1
#             coinCount += 1
#     return coinCount

def get_change(m):
    denominations = [1,5,10]
    coin_count = 0
    while m > 0:
        i = len(denominations)-1
        while i >= 0:
            while m >= denominations[i]:
                m = m - denominations[i]
                coin_count += 1
            i = i-1
    return coin_count

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
