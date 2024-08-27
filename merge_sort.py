def merge(arr, start, mid, end):
    left_arr = arr[start:mid+1]
    right_arr = arr[mid+1:end+1]

    i, j, k = 0, 0, start

    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1

    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1

    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1

def merge_sort(arr, start, end):
    if start < end:
        mid = (start + end) // 2
        merge_sort(arr, start, mid)
        merge_sort(arr, mid + 1, end)
        merge(arr, start, mid, end)

arr = [1, 5, 2, 3, 8, 25, 24, 36]
merge_sort(arr, 0, len(arr) - 1)
print(arr)