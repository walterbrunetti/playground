


def sum_n(n):

    total = 0

    for i in range(1, n + 1):
        total +=i
        print(i)
        print(' + ')

    return total

#print(sum_n(5))


def frog(X, Y, Z):
    r = X - Y
    if r < 1:
        return 1

    i, d = divmod(r, 1)

    return i + 1 if d > 0 else i


"""

  X = 10
  Y = 85
  D = 30

  r = 85 - 10 = 75

"""

#-----------------------------------------

"""
A[N] = each element is an itenger within the range [1..(N + 1)]
N is an integer within the range [0..100,000]
each element is distinct
each element of array A is an integer within the range [1..(N + 1)].


A = [2, 3, 1, 5]

"""

def find_missing_element(A):
    N = len(A) + 1  # one element is missing
    for i in range(1, N + 1):
        for count, j in enumerate(A):
            if i == j:
               break

        if count + 1 == len(A) and j != i:
            return i


def find_missing_element_fast(A):
    N = len(A) + 1  # one element is missing
    #result = sum([i for i in range(1, N + 1)])
    result = N*(N + 1) // 2
    return result - sum(A)

    

#A = [2, 3, 1, 4]
#print(find_missing_element_fast(A))


# -------------------------------

"""
- len(A) = N
- 0 < P < N
- splits A in two A[0], A[1], ..., A[P − 1] and A[P], A[P + 1], ..., A[N − 1]
- |(A[0] + A[1] + ... + A[P − 1]) − (A[P] + A[P + 1] + ... + A[N − 1])|
- return de minimal difference that can be achieved (P)
- Assumptions:
  * N is an integer within the range [2..100,000];
  * each element of array A is an integer within the range [−1,000..1,000].


[1, 2, 3, 4, 5, 6]

random medium, numbers from 0 to 100, length = ~10,000
✘
TIMEOUT ERROR
running time: 1.184 sec., time limit: 0.208 sec. 

"""


def tape_equilibrium(A):

    min_val = 1001
    N = len(A)

    for i in range(1, N - 1):
        a = sum(A[0:i])
        b = sum(A[i:N])

        r = abs(a-b)
        if r < min_val:
            min_val = r

    return min_val




A = [1, 1]
print(tape_equilibrium(A))




