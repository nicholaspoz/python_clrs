def merge(array, p, q, r):
    """
    Given an array A with sorted sub-sequences A[p...q] and A[q+1...r],
    merge them into a single sorted sequence A[p...r]
    """
    left = array[p:(q+1)]
    left.append(float("inf"))

    right = array[(q+1):(r+1)]
    right.append(float("inf"))

    i = j = 0
    for k in range(p, r+1):
        if left[i] < right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1

def merge_sort(array, p, r):
    q = (p + r) // 2

    if p == q:
        return
    else:
        merge_sort(array, p, q)
        merge_sort(array, q+1, r)
        merge(array, p, q, r)
