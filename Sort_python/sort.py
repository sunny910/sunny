def bubble_sort(nums):
    n = len(nums)
    for i in range(0, n):
        for j in range(0, n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums


def insert_sort(nums):
    n = len(nums)
    for i in range(1, n):
        key = nums[i]
        j = i-1
        while j >= 0:
            if key < nums[j]:
                nums[j+1] = nums[j]
                nums[j] = key
            j -= 1
    return nums


def select_sort(nums):
    n = len(nums)
    for i in range(0, n):
        index = i
        for j in range(i+1, n):
            if nums[j] < nums[index]:
                index = j
        nums[i], nums[index] = nums[index], nums[i]
    return nums


def quick_sort(nums, left, right):
    if left >= right:
        return nums
    low = left
    high = right
    key = nums[low]
    while low < high:
        while low < high and nums[high] > key:
            high -= 1
        if low < high:
            nums[low] = nums[high]
        while low < high and nums[low] < key:
            low += 1
        if low < high:
            nums[high] = nums[low]
    nums[low] = key
    quick_sort(nums, left, low-1)
    quick_sort(nums, low+1, right)
    return nums


def quick_partition(nums, low, high):
    key = nums[low]
    while low < high:
        while low < high and nums[high] > key:
            high -= 1
        if low < high:
            nums[low] = nums[high]
        while low < high and nums[low] < key:
            low += 1
        if low < high:
            nums[high] = nums[low]
    nums[low] = key
    return low


def quick_sort_p(nums, left, right):
    if left < right:
        mid = quick_partition(nums, left, right)
        quick_sort_p(nums, left, mid-1)
        quick_sort_p(nums, mid+1, right)
        return nums


def merge_sort(nums, left, right):
    if left < right:
        mid = (left+right)/2
        merge_sort(nums, left, mid)
        merge_sort(nums, mid+1, right)
        return merge(nums, left, mid, right)


def merge(nums, low, mid, high):
    left = nums[low:mid+1]
    right = nums[mid+1:high+1]
    i, j, k = low, 0, 0
    while (k < len(left)) and (j < len(right)):
        if left[k] <= right[j]:
            nums[i] = left[k]
            i += 1
            k += 1
        else:
            nums[i] = right[j]
            i += 1
            j += 1
    while k < len(left):
        nums[i] = left[k]
        i += 1
        k += 1
    while j < len(right):
        nums[i] = right[j]
        i += 1
        j += 1
    return nums


def merge_sort1(nums):
    if len(nums) <= 1:
        return nums
    n = len(nums)
    mid = (n-1)/2
    left = merge_sort1(nums[:mid+1])
    right = merge_sort1(nums[mid+1:])
    return merge1(left, right)


def merge1(left, right):
    i, j = 0, 0
    res = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    res += left[i:]
    res += right[j:]
    return res


def max_heap(nums, i, heap_size):
    lchild = 2*i+1
    rchild = 2*i+2
    largest = i
    if lchild < heap_size and nums[lchild] > nums[largest]:
        largest = lchild
    if rchild < heap_size and nums[rchild] > nums[largest]:
        largest = rchild
    if largest != i:
        nums[i], nums[largest] = nums[largest], nums[i]
        max_heap(nums, largest, heap_size)


def build_heap(nums, heap_size):
    for i in range(0,heap_size/2)[::-1]:
        max_heap(nums, i, heap_size)


def heap_sort(nums):
    heap_size = len(nums)
    build_heap(nums, heap_size)
    for i in range(0, heap_size)[::-1]:
        nums[0], nums[i] = nums[i], nums[0]
        max_heap(nums, 0, i)
