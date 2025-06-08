def solution(array):
    sorted_array = sorted(array)
    length = len(sorted_array)
    center = length //2
    median = sorted_array[center]
    return median