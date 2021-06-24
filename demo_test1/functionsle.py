# this is a class on functions
from calendar import calendar

# funtion to add 5
def addFive(x):
    num5= 5 + x
    return  num5
# to print calendarr

print(calendar(2021, 10))
# to check if its raining
def  weekDay():
    dayname1 = raw_input("Enter the day of the week: ")
    return  dayname1
provday = weekDay()
print str(provday)

print addFive(33)
# function to accept dynamic argument 
def addNumbers(*mutilnum):
    finalVal = 0
    if mutilnum:
        for i in mutilnum:
            finalVal += i
        return finalVal
    else:
        return 'Please enter a Number'

# function to print a dictionary
def dictionVal(**kvargs):
    for i in kvargs:
        print i, kvargs[i]
    return 

# recursion function for a factorial 
def factorialval(num):
    if num == 1:
        return 1
    else:
        # called the function name here        
        return num * factorialval(num - 1)
    
    
def main ():
    print addNumbers(23, 36,45,56,23,6,23,89)
    dictionVal(Cus1='Joy' , Cus2='James',  Cus3='Jerry')
    dictionVal(Cus1=('Joy' , 23), Cus2=('James', 34), Cus3=('Jerry', 38))
    print factorialval(5)

if __name__ == '__main__' : main()