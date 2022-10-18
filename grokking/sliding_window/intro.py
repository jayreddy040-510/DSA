#find the avgs of contiguous subarray of K elements

def find_avgs_of_subarray(arr, k):
    ret = []
    i = 0
    k_sum = sum([arr[x] for x in range(i,k)])
    ret.append(k_sum/(k-i))
    while k < len(arr):
        k_sum = k_sum - arr[i] + arr[k]
        ret.append(k_sum/(k-i))
        i, k = i+1, k+1
    return ret

print(find_avgs_of_subarray([1, 3, 2, 6, -1, 4, 1, 8, 2], 5))