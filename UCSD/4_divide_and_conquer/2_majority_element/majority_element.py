# Uses python3
import sys

# def get_majority_element(a, left, right):
#     if left == right:
#         return -1
#     if left + 1 == right:
#         return a[left]
#     #write your code here
#     return -1

import collections
def majority_candiate_hashmap( nums):
    counts = collections.Counter(nums)
    return max(counts.keys(), key=counts.get)

def majority_candiate_dAndc(nums, lo=0, hi=None):

    def majority_element_rec(lo, hi):
        # base case; the only element in an array of size 1 is the majority
        # element.
        if lo == hi:
            return nums[lo]
        # recurse on left and right halves of this slice.
        mid = (hi-lo)//2 + lo
        # print("mid ",mid)
        left = majority_element_rec(lo, mid)
        right = majority_element_rec(mid+1, hi)

        # print ("left --> ",left, "right --> ",right)

        # if the two halves agree on the majority element, return it.
        if left == right:
            return left

        # otherwise, count each element and return the "winner".
        left_count = sum(1 for i in range(lo, hi+1) if nums[i] == left)
        right_count = sum(1 for i in range(lo, hi+1) if nums[i] == right)
        # print("left_cout -- ",left_count, "right cout -- ",right_count)

        return left if left_count > right_count else right

    return majority_element_rec(0, len(nums)-1)

def majority_candiate( nums) -> int:
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        count += (1 if num == candidate else -1)

    return candidate

def get_majority_element(a):
    count = 0
    candidate = majority_candiate(a)
    for num in a:
        if candidate == num:
            count += 1

    if count > len(a)/2:
        return 1
    else:
        return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    # if get_majority_element(a, 0, n) != -1:
    #     print(1)
    # else:
    #     print(0)

    if get_majority_element(a) != -1:
        print(1)
    else:
        print(0)
