#Given an array of positive numbers and a positive number ‘k,’ find the maximum sum of any contiguous subarray of size ‘k’.

def max_sum_subarray(arr, k):
    max = float('-inf')
    i = 0
    k_sum = sum([arr[x] for x in range(i,k)])
    max = k_sum if k_sum > max else max
    while k < len(arr):
        k_sum = k_sum - arr[i] + arr[k]
        k, i = k + 1, i + 1
        max = k_sum if k_sum > max else max
    return max

print(max_sum_subarray([20, 1, 1, 7, 5, 22], 3))
