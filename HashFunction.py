import math
i=0
while i<2000:
    x=math.sqrt(i)
    x=math.sqrt(x)
    x=math.sqrt(x)
    x=math.sqrt(x)
    x=math.sqrt(x)
    x,y=math.modf(x)
    x=str(x)
    x=x.replace('0','')
    x=x[:7]
    x=sorted(x)
    x=''.join(x)
    if "234477" in x:print(i)
    i=i+1
