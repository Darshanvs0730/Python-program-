n = int(input("Enter the value of n: "))

r = int(input("Enter the value of r: "))

# Finding factorial using functions (recursive)

if n == 0 or n == 1:

return 1

else:

return n * fact(n-1)

n_minus_r = fact(n-r)

r_fact = fact(r)

print("Factorial: ", fact(n))

def fact(n):

print("Binomial Co-efficient: ", fact(n)/(n_minus_r*r_fact))

Enter the value of n: 5

Enter the value of r: 3

Factorial: 120

Binomial Co-efficient: 10.0

n = int(input("Enter the value of n: "))

a = 0

b = 1

count = 0

if n <= 0:

print("Please enter a valid integer")

elif n == 1:

print("Fibonacci series upto 1")

print(a)

else:
print("Fibonacci Sequence")

while (count < n):

print(a, end = " ")

c = a + b

# Updating the values of a and b by swapping

a = b

b = c

count += 1

Enter the value of n: 15

Fibonacci Sequence

0 1 1 2 3 5 8 13 21 34 55 89 144 233 377
