# A basic functional programming in Python


# a function to calculate a squared number
def square(n):
	return n ** 2

# Lambda expression to calculate a squared number
lambda_square = lambda x: x**2

print (square(5))
print (lambda_square(5))

# a recursive function to calculate the factorial of a number
def fat(n):
	if (n == 0): 
		return 1
	return (n * fat(n - 1))

# Lambda expression to calculate the factorial of a number
lambda_fat = lambda x: x * lambda_fat(x - 1) if x > 0 else 1

print (fat (5))
print (lambda_fat(5))

# Map: Apply function to every item of iterable and return a list of the results
l = [2, 4, 6, 8]
m = map(lambda x: x ** 2, l)
for i in m:
	print (i)

# Reduce: Performing some computation on a list and returning the result
# removed from python 3, to use we must import functools
from functools import reduce
print (reduce(lambda x, y: x + y, [1, 2, 3, 4, 5]))


# Filter: Creates a list of elements for which a function returns true
f = filter(lambda x: x % 2 == 0, range(10))
for i in f:
	print (i)