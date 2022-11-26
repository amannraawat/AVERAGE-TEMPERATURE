from array import *

print("\n\n\t\t\t\t\t\t\t\t\t **FIND NUMBER OF DAYS ABOVE TEMPERATURE** ")
day=int(input("\n\n\n\t\tHow many day's temperature ? "))


a=array('f')
for i in range(1,day+1):
    temp=input("\n\t\tDay {}'s high temperature:  ".format(i))
    value=float(temp)
    a.append(value)

average=sum(a)/len(a)
print("\n\n\t\t\t\t\t\t\t\t\t\t     Average: {:.2f}".format(average))

def findday_aboveavg(array1,value):
    total=0
    for i in array1:
        if i > value :
            total+=1
    return "\n\t\t\t\t\t\t\t\t\t\t{} day(s) above average".format(total)
    

print(findday_aboveavg(a,average))
