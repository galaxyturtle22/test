#import all the stuff
import time 
from time import perf_counter
import math
import sys

#set the max input value to infinity, however too large inputs(such as 1 mil) will quit the programm
sys.set_int_max_str_digits(0)

#set all the varuables
prev_num = 1
_2numago = 0
Fib_num = [1] #if I dont have the first value it will just omit it and be 1, 2, 3, 5... insted of 1, 1, 2, 3, 5...

#the function to calculate the number
#each time you run it it dose one more number
def calculate():
    global prev_num, _2numago, Fib_num

    prev_num = prev_num + int(_2numago)
    _2numago = prev_num - _2numago
    Fib_num.append(prev_num)

#ask how many
How_many = int(input("how many numbers do you want: "))
#start stopwatch
timeStart = perf_counter() 

#do all the calculations
for i in range(0, How_many-1, 1):
    calculate()

#stop stopwatch
timeEnd = perf_counter()


#print the values
print("The " + str(How_many) + "th Fibonacci is " + str(prev_num))
#                      round here so you don't get a sientific number
print("It took " + str(round(timeEnd-timeStart,5)) + " to calculate the " + str(How_many) + " Fibonacci number" )

#end statements for exiting and seeing the full sequence
while True:
    keyPress = input("Enter e to exit and s to see the sequence: ")
    if keyPress == "e":
        exit()
    elif keyPress == "s":
        print(Fib_num)




