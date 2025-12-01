def insertion_sort(arr: list[int]) -> list[int]:
    """Сортировка вставками.

    Returns:
        Отсортированный массив.
    """
    arr = arr[:]
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr