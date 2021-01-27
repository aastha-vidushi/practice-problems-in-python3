'''
FizzBuzz: Given an integer number n, for multiples of three print “Fizz” for the multiples of five print “Buzz”.
For numbers which are multiples of both three and five print “FizzBuzz”.

This is the Naive Approach, where simple if-else-condition is used inside the for-loop.
'''

print(__doc__)
def fizzBuzz(n):

    for i in range(1,n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(str(i))

fizzBuzz(100)