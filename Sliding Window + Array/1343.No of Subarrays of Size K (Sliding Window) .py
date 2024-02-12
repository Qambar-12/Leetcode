def numOfSubarrays(arr, k, threshold):
    count = 0
    current_window_sum = sum(arr[:k])
    if current_window_sum/k >= threshold:
        count += 1
    i, j = 0, k
    while j < len(arr):
        current_window_sum -= arr[i]
        current_window_sum += arr[j]
        if current_window_sum/k >=  threshold:
            count += 1
        i += 1
        j += 1
    return count

print(numOfSubarrays([2,2,2,2,5,5,5,8], 3, 4))  # Output: 3