#Given an array of positive numbers and a positive number ‘S,’ find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. Return 0 if no such subarray exists.


def smallest_sub_greater_sum(arr, S):
    ret = 0
    _sum = 0
    k = 0
    i = 0
    while k < len(arr):
        _sum += arr[k]
        while _sum >= S:
            if ret == 0 or 1 + k - i < ret:
                ret = k - i + 1
            _sum -= arr[i]
            i += 1
        k += 1
    return ret

    

# print(smallest_sub_greater_sum([1,1], 5))