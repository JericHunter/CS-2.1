#!python


def is_sorted(items):
    """Return a boolean indicating whether given items are in sorted order.
    TODO: Running time: O(N) Because we are looping through the array to find if arr is in sorted order
    TODO: Memory usage: O(1) not allocating any memory just checking if it's sorted"""
    # TODO: Check that all adjacent items are in order, return early if so
    isSorted = False

    while not isSorted:
        for i in range(len(items)):
            if items[i+1] < items[i]:
                return False
            else:
                return True

def bubble_sort(items):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    TODO: Running time:O(N) Because we are looping through the array to find if arr is in sorted order
    TODO: Memory usage:O(1) not allocating any memory just checking if it's sorted and then swapping"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Swap adjacent items that are out of order
    for i in range(len(items)):
        if items[i] > items[i+1]:
            items[i], items[i+1] = items[i+1], items[i]
    return items


def selection_sort(items):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: O(N)^2 Because we are looping through the array and we will have to keep iterating to keep finding the minimum
    TODO: Memory usage: O(1) not allocating any memory just checking if it's sorted and then swapping"""
    current = 0
    while current < len(items)-1:
        for i in range(current+1,len(items)):
        if items[i] < items[current]:
            items[current], items[i] = items[i], items[current]
        current+=1
    return items


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: O(N) Because we are looping through the array to find if arr is in sorted order
    TODO: Memory usage: O(1) not allocating any memory just checking if it's sorted and then swapping"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items
  for i in range(1,len(items)):
    while i > 0 and  items[i] < items[i-1]  :
      items[i], items[i-1] = items[i-1], items[i]
      i-=1
  return items
