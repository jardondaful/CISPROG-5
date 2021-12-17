a = int(input('Please input the smaller integer: '))
smaller = a
b = int(input('\nPlease input the larger integer: '))
larger = b
print("\nThis is the process of achieving the greatest common denominator of the two numbers: \n")
while a != 0:
    gcd = a
    print("The remainder of the larger number divided by the smaller number (which is " + str(b) + "/" + str(a) + ") is " + str(b%a))
    a = b % a
    b = gcd
    print("The larger number is " + str(b) + " and the smaller number is now " + str(a))
print("\nSince the smaller number is now 0, the process is done and the larger number is the greatest common divisor. This means that the greatest common divisor of the numbers " + str(smaller) + " and " + str(larger) + " is " + str(gcd))
