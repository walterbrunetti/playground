



def triangle(n):
    for i in range(1, n + 1):
        for j in range(i):
            print('*'),
        print

#triangle(4)


def upside_down_triangle(n):
    
    for i in range(1, n + 1):
        for h in range(0, i - 1):          
               print(' '),
        for j in range(0, 2*n - 2*i + 1):
            print('*'),
            
        print

#upside_down_triangle(5)

"""
rows n=4

1- no spaces - cantidad de (*) 2*n-1
2- 1 space - cantidad de (*) 2*n - 3
3- 2 spaces - cantidad de (*) 2*n - 5
4- 3 spaces - cantidad de (*) 2*n - 7


*******
 *****
  ***
   *
"""



def binary_gap(n):
    bin_n = "{0:b}".format(n)

    counter = 0
    start_counting = False
    max_counter = 0
    print(bin_n),
    for x in bin_n:
        if x == '1':
            start_counting = True
            if counter > max_counter:
                max_counter = counter
            counter = 0
            continue

        if start_counting and x == '0':
            counter += 1

    return max_counter

print(binary_gap(561892))
print(binary_gap(32))
print(binary_gap(9))
    

"""
001001000000


"""
