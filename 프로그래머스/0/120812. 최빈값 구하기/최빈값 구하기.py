def solution(array):
    mydic = dict()
    
    for i in range(len(array)):
        if array[i] in mydic:
            mydic[array[i]] += 1
        else:
            mydic[array[i]] = 1

    max_val = -1
    for key in mydic:
        if mydic[key] > max_val:
            max_val = mydic[key]

    cnt = 0
    max_key = -1
    for key in mydic:
        if mydic[key] == max_val:
            cnt += 1
            max_key = key

    if cnt != 1:
        return -1
    else:
        return max_key
