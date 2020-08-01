# python3

# def max_pairwise_product(numbers):
#     n = len(numbers)
#     max_product = 0
#     for first in range(n):
#         for second in range(first + 1, n):
#             max_product = max(max_product,
#                 numbers[first] * numbers[second])
#
#     return max_product

def max_pairwise_product(numbers):
    n = len(numbers)
    largest = 0
    second_largest = 0
    for i in range(0, n):
        if numbers[i] >= largest:
            second_largest = largest
            largest = numbers[i]
        elif numbers[i] > second_largest and numbers[i] < largest:
            second_largest = numbers[i]
    max_product = float(largest*second_largest)

    return int(max_product)


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
