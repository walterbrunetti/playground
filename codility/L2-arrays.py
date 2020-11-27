



def reverse_array(N):
    b = []    
    for i in range(len(N), 0, -1):
        b.append(N[i-1])

    return b


def reverse_array_2(N):
    
    for i in range(len(N) // 2):
        k = len(N) - i - 1
        temp = N[i]
        N[i] = N[k]
        N[k] = temp

    return N

a = [1, "2", 3, 4]

#print(reverse_array_2(a))

"""
a = [1, "2", 3, 4]

b = [4, 3, "2", 1]
"""



def cyclic_array(A, k):
    elements_count = len(A)

    b = ['X' for b in range(elements_count)]    
    for i in range(elements_count):
        if i + k < elements_count:
            b[i + k] = A[i]
        else:
            mod = (i + k) % elements_count
            b[mod] = A[i]

    return b

A = [3, 8, 9, 7, 6] 
K = 11
#print(A)
#print cyclic_array(A, K)

"""
the function should return [9, 7, 6, 3, 8]. Three rotations were made:
[3, 8, 9, 7, 6] -> [6, 3, 8, 9, 7]
[6, 3, 8, 9, 7] -> [7, 6, 3, 8, 9]
[7, 6, 3, 8, 9] -> [9, 7, 6, 3, 8]

val 9
Pos 2
Faltan 2
rotations 3
2 + 3 = 5

"""



def solution(A):

    s = set()
    for element in A:
        if element in s:
            s.remove(element)
        else:
            s.add(element)

    return s.pop()

A = [0 for n in range(13) ]
A[0] = 9; A[1] = 3;  A[2] = 9
A[3] = 3;  A[4] = 9;  A[5] = 7
A[6] = 9
A[7] = 19; A[8] = 13;  A[9] = 19
A[10] = 13;  A[11] = 192;  A[12] = 192

"""

the elements at indexes 0 and 2 have value 9,
the elements at indexes 1 and 3 have value 3,
the elements at indexes 4 and 6 have value 9,
the element at index 5 has value 7 and is unpaired.

all but one of the values in A occur an even number of times.


"""

print(solution(A))



