import timeit
import random

def insertion_sort(lst):
    """Implementation of insertion sort algorithm."""

    for i in range(1, len(lst)):
        key = lst[i]
        j = i-1
        while j >= 0 and key < lst[j] :
                lst[j+1] = lst[j]
                j -= 1
        lst[j+1] = key 
    return 

def merge_sort(arr):
    """Implementation of merge sort algorithm."""

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left, right):
    """Helper function to merge two sorted lists."""

    merged = []
    left_index = 0
    right_index = 0

    # Combine smaller elements first
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # If there are elements left in the left or right half, add them to the result
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged

def benchmark_sorting():
    """Benchmark insertion sort and merge sort algorithms."""

    sizes = [100, 1000, 5000, 10000]
    # Note: for Insertion Sort 5000 elements is already a lot for pure Python

    print(f"{'Algorithm':<20} | {'Size':<10} | {'Time (sec)':<15}")
    print("-" * 50)

    for size in sizes:
        data = [random.randint(0, 100000) for _ in range(size)]

        # Copying data for each sort to ensure fair comparison
        data_insertion = data.copy()
        data_merge = data.copy()
        data_timsort = data.copy()
        
        # Time for Insertion Sort
        if size <= 5000: 
            t_ins = timeit.timeit(lambda: insertion_sort(data_insertion), number=1)
            print(f"{'Insertion Sort':<20} | {size:<10} | {t_ins:.6f}")
        else:
            print(f"{'Insertion Sort':<20} | {size:<10} | {'Too slow'}")

        # Time for Merge Sort
        t_merge = timeit.timeit(lambda: merge_sort(data_merge), number=1)
        print(f"{'Merge Sort':<20} | {size:<10} | {t_merge:.6f}")

        # Time for Timsort (Python's built-in sort)
        t_tim = timeit.timeit(lambda: sorted(data_timsort), number=1)
        print(f"{'Timsort (Built-in)':<20} | {size:<10} | {t_tim:.6f}")
        
        print("-" * 50)

if __name__ == "__main__":
    benchmark_sorting()
