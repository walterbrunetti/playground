




def distinct(A):
    n = len(A)
    if n <= 1:
        return n

    A.sort()

    count = 1
    for i in range(1, n):
        if A[i-1] != A[i]:
            count +=1
    
    return count




#-------------------------------------#

def solution(A):
    n = len(A)
    result = []
    for i in range(n):
        range_a = (i-A[i], i+A[i])
        for j in range(n):
            if j == i:
                continue
            range_b = (j-A[j], j+A[j])
            if range_b[0] <= range_a[0] <= range_b[1] or range_b[0] <= range_a[1] <= range_b[1] or range_a[0] <= range_b[0] <= range_a[1] or range_a[0] <= range_b[1] <= range_a[1]:
                if j > i:
                    result.append((i, j))
                else:
                    result.append((j, i))

    if len(result) > 10000000:
        return -1

    return len(set(result))


def solution_2(A):
    circle_endpoints = []
    for i, a in enumerate(A):
        circle_endpoints += [(i-a, True), (i+a, False)]
 
    circle_endpoints.sort(key=lambda x: (x[0], not x[1]))
 
    intersections, active_circles = 0, 0
 
    for _, is_beginning in circle_endpoints:
        if is_beginning:
            intersections += active_circles
            active_circles += 1
        else:
            active_circles -= 1
        if intersections > 10E6:
            return -1
 
    return intersections

A = [1, 5, 2, 1, 4, 0]
print(solution(A))
print(solution_2(A))
