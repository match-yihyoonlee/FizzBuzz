import sys

if len(sys.argv) > 1:
    n = int(sys.argv[1])
elif len(sys.argv) == 1:
    n = int(raw_input("What is the Upper Range for Fizz Buzz Game?: "))

for i in range(1,n+1):
    print "Fizz buzz counting up to {}".format(i)

    if i % 3 == 0 and i % 5 == 0:
        print "fizz buzz"

    elif i % 3 == 0:
        print  "fizz"

    elif i % 5 == 0:
        print "buzz"

    else:
        print i

