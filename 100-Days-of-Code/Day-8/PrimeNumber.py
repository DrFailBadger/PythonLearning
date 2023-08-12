#https://www.geeksforgeeks.org/prime-numbers/
 
# import sqrt from math module
from math import sqrt
 
 
 
# Function check whether a number
# is prime or not
def isPrime(n):
 
    # Corner case
    if (n <= 1):
        print ("Not a Prime Number")
        return False
 
    # Check from 2 to sqrt(n)
    for i in range(2, int(sqrt(n))+1):
        if (n % i == 0):
            print ("Not a Prime Number")
            return False
    print ("It is a Prime Number")
    return True
inputNumber = int(input("Check this number: "))
isPrime(inputNumber)
# # Driver Code
# if __name__ == '__main__':
#     if isPrime(11):
#         print("true")
#     else:
#         print("false")
 