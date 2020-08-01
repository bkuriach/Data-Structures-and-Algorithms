# Uses python3
import sys
# capacity = 50
# weights = [20,50,30]#[10, 40, 20, 30]
# values = [60,100,120]#[60, 40, 100, 120]

def insertionSort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key.cost > arr[j].cost:
            temp = arr[j+1]
            arr[j + 1] = arr[j]
            arr[j]=temp
            j -= 1
        # arr[j + 1] = temp
    return  arr


class ItemValue:
    """Item Value DataClass"""

    def __init__(self, wt, val, ind):
        self.wt = wt
        self.val = val
        self.ind = ind
        self.cost = val / wt

    def __lt__(self, other):
        return self.cost < other.cost

def get_optimal_value(capacity, weights, values):
    value = 0.
    unit_values = []
    for i in range(len(values)):
        unit_values.append(ItemValue(weights[i],values[i],i))
    # unit_values.sort(reverse=True)
    unit_values = insertionSort(unit_values)
    for i in unit_values:
        # print(i.cost,i.val,i.ind)
        if i.wt <= capacity:
            capacity -= i.wt
            value += i.val
        else:
            value = value + ((capacity/i.wt) * i.val)
            capacity = capacity - (capacity/i.wt) * i.wt
            break

    return value

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
