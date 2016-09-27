import matplotlib.pyplot as plot
import math
from numpy import arange
myname = raw_input("What is your name? ")
def hello(name):
    print "Hello %s" % name

hello(myname)


def f(x):
    return x + 1

xs = range(-3, 4)
ys = []
for x in xs:
    ys.append(f(x))

plot.plot(xs, ys)
plot.show()

def f(x):
    return x * x

xs = range(-100, 101)
ys = []
for x in xs:
    ys.append(f(x))

plot.plot(xs, ys)
plot.show()

def f(x):
    if x % 2 == 0:
        return -1
    else:
        return 1

xs = range(-5, 6)
ys = []
for x in xs:
    ys.append(f(x))

plot.bar(xs, ys)
plot.show()


def f(x):
    return math.sin(x)

xs = range(-5, 6)
ys = []
for x in xs:
    ys.append(f(x))

plot.plot(xs, ys)
plot.show()

def f(x):
    return math.sin(x)

xs = arange(-5, 6, 0.1)
ys = []
for x in xs:
    ys.append(f(x))

plot.plot(xs, ys)
plot.show()

def f(x):

    return (x * 1.8) + 32

xs = range(-20, 120)
ys = []
for x in xs:
    ys.append(f(x))

plot.plot(xs, ys)
plot.show()




def again():
    playagain = raw_input("Do you want to play again? (Y or N) ")
    if playagain == "Y":
        return True
    elif playagain == "N"
        return False
    else:
        print "Invalid input"
        return playagain

again()
