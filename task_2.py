from task_1 import merge

def merge_k_lists(lists):
    """Merge k sorted lists and return them as a one sorted list."""
    
    if not lists:
        return []
    
    # Base case: if there is only one list left, return it
    if len(lists) == 1:
        return lists[0]
    
    mid = len(lists) // 2
    left_merged = merge_k_lists(lists[:mid])
    right_merged = merge_k_lists(lists[mid:])

    return merge(left_merged, right_merged)

if __name__ == "__main__":
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    merged_list = merge_k_lists(lists)
    print("Відсортований список:", merged_list)