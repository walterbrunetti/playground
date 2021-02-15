




"""

"""



def prefix_sums(A):
    n = len(A)
    P = [0] * (n + 1)
    for k in range(1, n + 1):  # n+1 = 5
        print(k)
        P[k] = P[k - 1] + A[k - 1]
    return P

A = [1, 4, 2, 5]
#print(prefix_sums(A))




#------------------------------------------------------------#

"""
A and B are integers within the range [0..2,000,000,000];
K is an integer within the range [1..2,000,000,000];
A ≤ B.


"""

def count_div_solution(A, B, K):
    if K > B:
        return 0

    N = B - A + 1
    if K == 1:
        return N

    start = A
    if K > A:
        start = K

    counter = 0
    for i in range(start, B + 1):
        if i % K == 0:
            counter +=1
            
    return counter


def count_div_solution_2(A, B, K):
    if K > B:
        return 0

    N = B - A + 1
    if K == 1:
        return N

    tot = B // K - A // K
    if A % K == 0:
        return tot + 1

    return tot



#print(count_div_solution(1, 1, 11))
#print(count_div_solution_2(1, 1, 11))






#------------------------------------------------------------#
"""


N is an integer within the range [1..100,000];
M is an integer within the range [1..50,000];
each element of arrays P, Q is an integer within the range [0..N − 1];
P[K] ≤ Q[K], where 0 ≤ K < M;
string S consists only of upper-case English letters A, C, G, T.


"""

def solution(S, P, Q):
    N = len(P)
    result = []
    DNA_CONST = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    for i in range(N):
        dna_part = S[P[i]:Q[i] + 1]
        part_len = Q[i] - P[i] + 1
        dna = DNA_CONST.get(dna_part[0])
        min_dna = dna
        j = 0
        while dna > 1 and j < part_len - 1:
            if dna < min_dna:
                min_dna = dna
            j += 1
            dna = DNA_CONST.get(dna_part[j])
        result.append(min(min_dna, dna))

    return result

def solution_2(S, P, Q):
    N = len(P)
    result = []
    S = S.replace('A', '1').replace('C', '2').replace('G', '3').replace('T', '4')
    S = list(map(int, S))
    for i in range(N):
        dna_part = S[P[i]:Q[i] + 1]
        part_len = Q[i] - P[i] + 1
        dna = dna_part[0]
        min_dna = dna
        j = 0
        while dna > 1 and j < part_len - 1:
            if dna < min_dna:
                min_dna = dna
            j += 1
            dna = dna_part[j]
        result.append(min(min_dna, dna))

    return result


def solution_3(S, P, Q):
    
    N = len(S)
    A = [0] * (N + 1)
    C = [0] * (N + 1)
    G = [0] * (N + 1)
    for i in range(1, len(S) + 1):
        dna = S[i - 1]
                
        A[i] = A[i-1] + (1 if dna == 'A' else 0)
        C[i] = C[i-1] + (1 if dna == 'C' else 0)
        G[i] = G[i-1] + (1 if dna == 'G' else 0)

    result = []
    for i in range(len(P)):
        val = A[Q[i] + 1] - A[P[i]]
        if val > 0:
            result.append(1)
            continue
        val = C[Q[i] + 1] - C[P[i]]
        if val > 0:
            result.append(2)
            continue
        val = G[Q[i] + 1] - G[P[i]]
        if val > 0:
            result.append(3)
            continue
        result.append(4)

    return result




from time import perf_counter
from random import randrange
DNA = ['A', 'C', 'G', 'T']
test = ''
for i in range(100000):
    test += DNA[randrange(4)]

t1_start = perf_counter() 

print(solution('ACTGCCAGT', [2, 5, 0, 4, 3, 8, 0, 2, 0], [4, 5, 6, 8, 8, 8, 8, 5, 0]))
#print(solution_2(test, [2, 5, 0], [4, 5, 6]))
print(solution_3('ACTGCCAGT', [2, 5, 0, 4, 3, 8, 0, 2, 0], [4, 5, 6, 8, 8, 8, 8, 5, 0]))

t1_stop = perf_counter() 

print("Elapsed time during the whole program in seconds:",  t1_stop-t1_start) 

