"""
Write a menu drive program to do the following:
1. To accept a number as parameter to the function prime() and return 1 if the number is prime else return 0.
2. To accept the number of terms to the function series() and return the sum.
"""


def prime(n=10):
    c = 0
    for i in range(1, n + 1):
        if n % i == 0:
            c += 1
    if c == 2:
        return 1
    else:
        return 0


def series(n=10):
    sign = 1
    fact = 1
    s = 0
    for i in range(1, n + 1):
        fact = fact * 1
        s += sign * fact / i
        sign = sign * - 1
    return s


print('Select an option')
print('1. Check Prime')
print('2. Series Sum')
ch = int(input('Enter an option: '))
k = ""
if ch == 1:
    n = input('Enter a number or if you want to skip press Enter: ')
    if n.isdigit():
        k = prime(int(n))
    if k == 1:
        print('It is prime number ', n)
    else:
        print('It is not a prime number ', n)
elif ch == 2:
    n = input('Enter a number if you want or skip press Enter: ')
    if n.isdigit():
        s = series(int(n))
    else:
        s = series()
    print('Sum of series is: ', s)
else:
    print('Invalid option')
