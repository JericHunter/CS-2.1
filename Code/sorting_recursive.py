#!python


def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until one list is empty
    # TODO: Find minimum item in both lists and append it to new list
    # TODO: Append remaining items in non-empty list to new list


def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Split items list into approximately equal halves
    # TODO: Sort each half using any other sorting algorithm
    # TODO: Merge sorted halves into one list in sorted order


def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # If the list is a single element, return it
    if len(items) <= 1:
        return items

    mid = len(items) // 2

    # Recursively sort and merge each half
    left_list = merge_sort(items[:mid])
    right_list = merge_sort(items[mid:])

    # Merge the sorted lists into a new one
    return _merge(left_list, right_list)


def _merge(left_list, right_list):
    result = []
    left_index, right_index = 0, 0

    for i in range(len(left_list) + len(right_list)):
        if left_index < len(left_list) and r_index < len(right_list):

            # If the item at the beginning of the left list is smaller, add it to the sorted list
            if left_list[left_index] <= right_list[right_index]:
                result.append(left_list[left_index])
                left_index += 1

            # If the item at the beginning of the right list is smaller, add it to the sorted list
            else:
                result.append(right_list[right_index])
                right_index += 1

        # If we have reached the end of the of the left list, add the elements from the right list
        elif l_index == len(l_list):
            result.append(right_list[right_index])
            right_index += 1

        # If we have reached the end of the of the right list, add the elements from the left list
        elif right_index == len(right_list):
            result.append(left_list[left_index])
            left_index += 1

    return result


def partition(items, low, high):
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    pivot = items[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while items[i] < pivot:
            i += 1

        j -= 1
        while items[j] > pivot:
            j -= 1

        if i >= j:
            return j

        # Swap
        items[i], items[j] = items[j], items[i]



def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    quick_sort_helper(items, 0, len(items) - 1)


def quick_sort_helper(items, low, high):
    if low < high:
        split_point = partition(items, low, high)
        quick_sort_helper(items, low, split_point)
        quick_sort_helper(items, split_point + 1, high)
