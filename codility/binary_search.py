






def binary_search(l, result, low=None, high=None):

    if not low:
        low = 0

    if not high:
        high = len(l) - 1


    mid = (low + high) // 2

    if high < low:
        return -1


    if l[mid] == result:
        return mid


    if l[mid] < result:
        low = mid + 1
        return binary_search(l, result, low, high)


    else:
        # med is greater
        high = mid - 1
        return binary_search(l, result, low, high)

    return -1



if __name__ == "__main__":


    l = [1, 2, 4, 5, 6, 12, 14, 15]

    print(binary_search(l, 37))


    
