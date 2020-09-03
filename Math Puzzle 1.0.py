import math

def xrunthrough():
    x=0
    y=0
    num=0
    tot=[x,y]
    day=0
    days=100
    howmany=1000000
    firstday=True
    right=[]
    total=0
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
xrunthrough()
