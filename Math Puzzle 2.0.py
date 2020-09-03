import matplotlib.pyplot as plt
import time
import sys
import math
#initializing all the variables used
#BTW all the methods have all the variables because I was too stupid to realize you can make a variable global until like a couple weeks ago
def startup():
    x=1
    y=0
    num=0
    numx=0
    numy=0
    tot=[x,y]
    day=0
    days=100
    howmany=0
    printed=False
    choice=input('1 or 2 or 3\n1 is fast\n2 is slow\n3 is inputmode\n')
    #Fast Mode
    if choice=='1':
        howmany=int(input("How many numbers should I look through\n"))
        seconds = 300*(howmany/150)
        minutes = seconds/60
        hours = minutes/60
        tdays = hours/24
        starttime=time.time()
        firstday=True
        right=[]
        total=0
        fastmode(x,y,total,numx,numy,howmany,days,day,right,starttime,printed)
    #Slow Mode
    elif choice=='2':
        howmany=int(input("How many numbers should I look through\n"))
        seconds = 300*(howmany/150)
        minutes = seconds/60
        hours = minutes/60
        tdays = hours/24
        starttime=time.time()
        firstday=True
        right=[]
        total=0
        #WIP DOES NOT WORK AT ALL unless you use huge numbers
        print('That will take about\n' + str(seconds) + 'seconds\n' + str(minutes) + ' minutes\n' + str(hours) + " hours\n" + str(tdays) + ' days\n')
        choice=input('Are you sure that you want to do that?\n')
        #Just so user can input anything that starts with y and it will register and a yes
        if 'y' in choice or 'Y' in choice:
            main(x,y,total,numx,numy,howmany,days,day,right,starttime,printed)
        else:startup()
    #Input Mode
    elif choice=='3':
        starttime=time.time()
        firstday=True
        right=[]
        total=0
        inputmode(x,y,total,numx,numy,howmany,days,day,right,starttime,printed)
#Useless just too lazy to take out and afraid it will break something
def main(x,y,total,numx,numy,howmany,days,day,right,starttime,printed):
    xrun(x,y,total,numx,numy,howmany,days,day,right,starttime,printed)

#Runs all x or first values after running all y values Ex. 1:1 2:1 3:1
def xrun(x,y,total,numx,numy,howmany,days,day,right,starttime,printed):
    for numx in range(howmany):
        numx=numx+1
        x=x+1
        yrun(x,y,total,numx,numy,howmany,days,day,right,starttime,printed)
    print(right)
    print("That took ",time.time()-starttime," seconds")
#Runs all y or secondary values Ex. 1:1 1:2 1:3
def yrun(x,y,total,numx,numy,howmany,days,day,right,starttime,printed):
    for numy in range(howmany):
        numy=numy+1
        y=y+1
        dayrun(x,y,total,numx,numy,howmany,days,day,right,starttime,printed)
#Actually performing the calculations
def dayrun(x,y,total,numx,numy,howmany,days,day,right,starttime,printed):
    secondday=True
    day=1
    tot=[x]
    total=x
    print("\n")
    for day in range(days):
        day=day+1
        print(numx,numy,day,total)
        if secondday==True:
            tot.append(y)
            secondday=False
        last=tot[-1]
        seclast=tot[-2]
        tot.append(seclast+last)
        total=seclast+last
        if total==1000000:
            day=day+1
            print(numx,numy,day,total)
            print('Started with ' + str(y), 'and ' + str(x) + ' Day',day)
            right.append("X Value = " + str(y) + " Y Value = " + str(x) + ' ' + str(day) + " days")
            break
        if total>5000000:
            break
    return x,y,total
# Samething as slow except x and y values are linked together Ex. 1:1 2:2 3:3
def fastmode(x,y,total,numx,numy,howmany,days,day,right,starttime,printed):
    for num in range(howmany):
        if total==1000000:
            print('Done','Started with' + str(x), 'Started with' + str(y),day)
            right.append(x)
        firstday=True
        day=0
        num=num+1
        x=x+1
        y=y+1
        for day in range(days):
            if firstday==True:
                tot=[x,y]
                firstday=False
            seclast=tot[-1]
            last=tot[-2]
            tot.append(seclast+last)
            total=seclast+last
            if total==1000000:
                break
            if total>1000000:
                break
            day=day+1
            print(num,day,total)
            x=x+1
            y=y+1
    print(right)
    print("That took ",time.time()-starttime," seconds")
#Input two values to see if they work/if the program works
def inputmode(x,y,total,numx,numy,howmany,days,day,right,starttime,printed):
    y=input("What is the first deposit?\n")
    x=input("what is the second deposit?\n")
    x = int(x)
    y = int(y)
    day=1
    inputdayrun(x,y,total,numx,numy,howmany,days,day,right,starttime,printed)
#Running calculations of input values
def inputdayrun(x,y,total,numx,numy,howmany,days,day,right,starttime,printed):
    secondday=True
    day=1
    tot=[x]
    total=x
    print("\n")
    for day in range(days):
        day=day+1
        print(day,total)
        if secondday==True:
            tot.append(y)
            secondday=False
        last=tot[-1]
        seclast=tot[-2]
        tot.append(seclast+last)
        total=seclast+last
        if total==1000000:
            day=day+1
            print(day,total)
            print('Started with ' + str(y), 'and ' + str(x) + ' Day',day)
            right.append("X Value = " + str(y) + " Y Value = " + str(x) + ' ' + str(day) + " days")
            break
        if total>5000000:
            break
    return x,y,total

startup()
