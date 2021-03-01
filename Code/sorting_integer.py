#!python

from sorting_iterative import insertion_sort

def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.
    TODO: Running time: O(n+k) the algorithm goes through n+k times
    TODO: Memory usage:  O(max) the bigger size the range of elements, larger is the space complexity"""
    # TODO: Find range of given numbers (minimum and maximum integer values)
    # TODO: Create list of counts with a slot for each number in input range
    # TODO: Loop over given numbers and increment each number's count
    # TODO: Loop over counts and append that many numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list
    max_num = max(numbers)
    count = [0] * max_num # generates maximum amount of 0's
    
    for num in numbers:
        count[num] += 1 # store each occurence
    
    i = 0
    
    for val in range(m+1):
        for _ in range(count[val]):
            numbers[i] = val
            wirte_pos += 1

def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    TODO: Running time: O(n+k) best case because it occurs when the elements are uniformly distributed in the buckets with a nearly equal number of elements in each bucket.
    TODO: Memory usage: O(n+k) storing nums and buckets"""
    # TODO: Find range of given numbers (minimum and maximum values)
    # TODO: Create list of buckets to store numbers in subranges of input range
    # TODO: Loop over given numbers and place each item in appropriate bucket
    # TODO: Sort each bucket using any sorting algorithm (recursive or another)
    # TODO: Loop over buckets and append each bucket's numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list
    bucket = []

    # Create empty buckets
    for i in range(num_buckets)):
        bucket.append([])

    # Insert elements into their respective buckets
    for j in numbers:
        index_b = int(10 * j)
        bucket[index_b].append(j)

    # Sort individual buckets 
    for i in num_buckets
        bucket[i] = insertionSort(bucket[i])

    # Get the sorted elements
    k = 0
    for i in range(len(num_buckets)):
        for j in range(len(bucket[i])):
            numbers[k] = bucket[i][j]
            k += 1
    return numbers
