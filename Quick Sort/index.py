def quick_sort(arr, low, high):
    pivot = partition(arr, low, high)
    quick_sort(arr, low, pivot)
    quick_sort(arr, pivot + 1, high)
    return


def swap(arr, elem1, elem2):
    temp = arr[elem1]
    arr[elem1] = arr[elem2]
    arr[elem2] = temp


def partition(arr, low, high):
    pivot = arr[low]
    print("arr", pivot)
    i = low
    j = high
    while i < j:
        while i <= j and arr[j] >= pivot:
            j = j - 1

        while i <= j and arr[i] <= pivot:
            i = i + 1

        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break
    print("arr", i, j, pivot)
    arr[low], arr[j] = arr[j], arr[low]
    # swap(arr, pivot, j)
    return j


list_arr = [7, 3, 4, 2, 5, 10, 5]

result = quick_sort(list_arr, 0, len(list_arr)-1)
print(list_arr)
