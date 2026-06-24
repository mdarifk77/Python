# factorial using function and recursion.

# def factorial(n):
#     if(n==1 or n==0):
#         return 1
#     return n * factorial(n-1)
# n = int(input("Enter the number: "))
# print(f"the factorial of {n} is {factorial(n)}")

# find greatest of three numbers using function.

def greater (a, b, c):
    if (a>b and a>c):
        return a
    elif (b>a and b>c):
        return b
    elif (c>a and c>b):
        return c
m = int(input("Enter the first number: "))
n = int(input("Enter the second number: "))
o = int(input("Enter the thirtd number: "))
print(f"The greatest number is {greater(m, n, o)}")