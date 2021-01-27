'''
FizzBuzz: Given an integer number n, for multiples of three print “Fizz” for the multiples of five print “Buzz”.
For numbers which are multiples of both three and five print “FizzBuzz”.

This is a better Approach, where modulo (%) operator is not used for comparison
'''

print(__doc__)
def fizzBuzz(n):

    c3=0
    c5=0

    for i in range(1,n+1):
        c3 = c3+1
        c5 = c5+1
        data = ""

        if c3 == 3:
            data = "Fizz"
            c3=0
        if c5 == 5:
            data += "Buzz"
            c5=0
        if data == "":
            print(str(i))
        else:
            print(data)

fizzBuzz(15)