

"""
X, Y, Z inital amount of fuel on each dispenser

For example, given X = 7, Y = 11, Z = 3 and the following array A:
A[0] = 2
A[1] = 8
A[2] = 4
A[3] = 3
A[4] = 2

returns 8 as The subsequent cars will have to wait in the queue for 0, 0, 2, 2 and 8 seconds, respectively.

Assume:
    - tanking one liter of fuel takes exactly one second
    - moving cars is instantaneous
    - N is an integer within the range [1.. 100,000);
    - each element of array A is an integer within the range [1.. 1,000,000,000];
    - X, Y and Z are integers within the range [0.. 1,000,000,000].

"""


def solution(A, X, Y, Z):
    """
        returns maximun amount of time for a car.
        If any car is unable to refuel, the function should return - 1.
    """
    i = 0
    X_time_left = 0
    Y_time_left = 0
    Z_time_left = 0
    wait = 0
    while i <= len(A) - 1:
        car_fuel = A[i]
        if X - car_fuel >= 0 and is_dispenser_free(X_time_left):
            X -= car_fuel
            X_time_left = car_fuel
            i +=1
        elif Y - car_fuel >= 0 and is_dispenser_free(Y_time_left):
            Y -= car_fuel
            Y_time_left = car_fuel
            i +=1
        elif Z - car_fuel >= 0 and is_dispenser_free(Z_time_left):
            Z -= car_fuel
            Z_time_left = car_fuel
            i +=1
        else:
            if all((is_dispenser_free(X_time_left), is_dispenser_free(Y_time_left), is_dispenser_free(Z_time_left))):
                return -1
            wait +=1
            X_time_left -= 1
            Y_time_left -= 1
            Z_time_left -= 1

                

    return wait
            

def is_dispenser_free(dispenser):
    return dispenser <= 0




X = 7
Y = 11
Z = 3
A = [2, 8, 4, 3, 2]


resp = solution(A, X, Y, Z)
print(resp)
assert(resp == 8)


X = 3
Y = 0
Z = 4
A = [5]

resp = solution(A, X, Y, Z)
print(resp)
assert(resp == -1)


