import matplotlib.pyplot as plt
import time
import math
#Hi yea I'm too lazy to go through all the code again but TLDR its the exact same thing except it can spit it out to a graph
def startup():
    x=1
    y=0
    num=0
    numx=0
    numy=0
    tot=[x,y]
    day=0
    days=100
    choice=input('1 or 2\n1 is fast\n2 is slow\n')
    howmany=int(input("How many numbers should I look through\n"))
    seconds = 300*(howmany*30)
    minutes = seconds/60
    hours = minutes/60
    tdays = hours/24
    starttime=time.time()
    firstday=True
    right=[]
    total=0
    if choice=='1':
        fastmode(x,y,total,numx,numy,howmany,days,day,right,starttime)
    elif choice=='2':
        print('That will take about\n' + str(seconds) + 'seconds\n' + str(minutes) + ' minutes\n' + str(hours) + " hours\n" + str(tdays) + ' days\n')
        choice=input('Are you sure that you want to do that?\n')
        if 'y' in choice or 'Y' in choice:
            main(x,y,total,numx,numy,howmany,days,day,right,starttime)
        else:startup()
def main(x,y,total,numx,numy,howmany,days,day,right,starttime):
    xrun(x,y,total,numx,numy,howmany,days,day,right,starttime)


def xrun(x,y,total,numx,numy,howmany,days,day,right,starttime):
    for numx in range(howmany):
        numx=numx+1
        x=x+1
        yrun(x,y,total,numx,numy,howmany,days,day,right,starttime)
        dayrun(x,y,total,numx,numy,howmany,days,day,right,starttime)


def yrun(x,y,total,numx,numy,howmany,days,day,right,starttime):
    for numy in range(howmany):
        numy=numy+1
        y=y+1
        dayrun(x,y,total,numx,numy,howmany,days,day,right,starttime)
    print(right)
    print("That took ",time.time()-starttime," seconds")


def dayrun(x,y,total,numx,numy,howmany,days,day,right,starttime):
    firstday=True
    day=0
    for day in range(days):
        if firstday==True:
            tot=[x,y]
            firstday=False
        seclast=tot[-1]
        last=tot[-2]
        tot.append(seclast+last)
        total=seclast+last
        if total==1000000:
            print('Started with' + str(x), 'Started with' + str(y),day)
            right.append("X Value = " + str(x) + " Y Value = " + str(y) + ' ' + str(day) + " days")
        if total>5000000:
            break

        day=day+1
        print(numx,numy,day,total)
        x=x+1
        y=y+1
    return x,y,total
def fastmode(x,y,total,numx,numy,howmany,days,day,right,starttime):
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

def calculate():
    times=[]
    howmanys=[]
    x=1
    y=0
    num=0
    numx=0
    numy=0
    tot=[x,y]
    day=0
    days=100
    howmany=0
    seconds = 300*(howmany/100000)
    minutes = seconds/60
    hours = minutes/60
    tdays = hours/24
    starttime=time.time()
    firstday=True
    right=[]
    total=0
    while howmany in range(100):
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
        totaltime=time.time()-starttime
        print("That took ",totaltime," seconds")
        howmany=howmany+1
        times.append(totaltime)
        howmanys.append(howmany-1)
    plt.plot(howmanys,times)
    plt.ylabel("How many numbers")
    plt.xlabel('Time')
    plt.show()

calculate()
