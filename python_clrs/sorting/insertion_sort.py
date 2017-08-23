def insertion_sort(array):
    """
    Sorts an array in-place.

    For each element, compare the current value to previous elements, shifting them up one index,
    until a smaller value is found - then put the current value in that final index.
    """
    for index in range(1, len(array)):
        key = array[index]
        i = index - 1
        while i >= 0 and key < array[i]:
            array[i+1] = array[i]
            i -= 1
        array[i+1] = key

    return array
