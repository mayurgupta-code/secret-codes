# to import Calc
import Calc 
# to import a specific function or class from Calc module
from Calc import add
# to import all functions of the Calc
from Calc import *

a = 9 
b = 7

c = Calc.add(a,b)
# print(c)

d = multi(a,b)
# print(d)

print("demo says:" + __name__)

# __name__ is a variable that defines the point of the 
# execution of the python code
# this is like from where the code starts
# as if i starts this code from Calc then hello __main__ is there
# and if import Calc module in demo module or somewhere else then Calc is printed