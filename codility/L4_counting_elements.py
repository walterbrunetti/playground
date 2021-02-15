





"""
N and X are integers within the range [1..100,000];
each element of array A is an integer within the range [1..X].



"""

def find_earliest_time_frog_can_jump(X, A):
    n = len(A)
    count = [0] * X
    tot = 0
    for i in range(n):
        if count[A[i] - 1]:
            continue
        count[A[i] - 1] = 1
        tot +=1
        if tot == X:
            return i
    return -1

A = [1, 3, 1, 4, 2, 3, 5, 4]
#find_earliest_time_frog_can_jump(A)




#-----------------------------------------


"""
N and M are integers within the range [1..100,000];
each element of array A is an integer within the range [1..N + 1].


"""

def max_counters(N, A):
    count = [0] * N
    max_counter = 0

    for ele in A:
        if ele == N + 1:
            count = [max_counter] * N
            continue
        count[ele - 1] +=1
        if count[ele-1] > max_counter:
            max_counter = count[ele-1]

    return count


A = [3, 4, 4, 6, 1, 4, 4]



#-----------------------------------------


"""
N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].

"""

def solution(A):
    _max = max(A)
    if _max <= 0:
        return 1

    count = [0] * _max

    for ele in A:
        if ele <= 0:
            continue
        count[ele - 1] +=1

    count.append(0)

    i = 0
    n = count[i]
    while n > 0:
        i += 1
        n = count[i]

    return i + 1

        
