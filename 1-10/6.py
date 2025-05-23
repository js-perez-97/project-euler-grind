# 6. Sum square Difference
# https://projecteuler.net/problem=6

def sum_square_difference(num):
    sum_of_squares = sum(i**2 for i in range(1, num+1))
    square_of_sum = sum(range(1, num+1))**2
    return square_of_sum - sum_of_squares

print(sum_square_difference(100))
