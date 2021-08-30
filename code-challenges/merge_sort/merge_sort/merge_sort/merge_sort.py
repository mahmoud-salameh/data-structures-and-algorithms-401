def merge_sort(arr):
    n = len(arr)
    if n >1:
        mid = int(n/2)
        L = arr[0:mid]
        R = arr[mid:n]
        merge_sort(L)
        merge_sort(R)
        merge(L, R, arr)
    return arr

def merge(L, R, arr):
    i = 0
    j = 0
    k = 0
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i= i + 1
        else:
            arr[k] = R[j]
            j= j +1
        k = k+1

    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1