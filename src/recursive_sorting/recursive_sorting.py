# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here
    i = 0
    j = 0
    k = 0

    while i < len(arrA) and j < len(arrB):
        if arr1[i] < arr[2]:
            merged_arr[k] = arrA[i]
            k = k + 1
            i = i + 1
        else: 
            merged_arr[k] = arrB[j]
            k = k + 1
            j = j + 1
    while i < len(arrA):
        merged_arr[k] = arrA[i]
        k = k + 1
        i = i + 1
    while j < len(arrB):
        merged_arr[k] = arrB[j]
        k = k + 1
        j = j + 1
        

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # Your code here


    return arr


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    start2 = mid + 1
    if arr[mid] <= arr[start2]:
        return 
    while start <= mid and start2 <= end:
        if arr[start] <= arr[start2]:
            start += 1
        else: 
            value = arr[start2]
            index = start2
            while index != start:
                arr[index] = arr[index - 1]
                index -= 1
            arr[start] = value
            start += 1
            mid += 1
            start2 += 1


    # return arr


def merge_sort_in_place(arr, l, r):
    # Your code here
    if l < r:
        m = l + (r - l) // 2
        merge_sort_in_place(arr, l, m)
        merge_sort_in_place(arr, m + 1, r)
        merge_in_place(arr, l, m, r)


    # return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
