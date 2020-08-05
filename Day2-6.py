x=[]
scr=[]
total=0
a=0
high=0
low=999
p=input("請輸入人數")
p=int(p)
for i in range(p):
    n=input("請輸入名字")
    x.append(n)
    s=input("請輸入分數")
    s=int(s)
    scr.append(s)
for i in range(p):
    total=total+scr[i]
    if scr[i] > high:
        high=scr[i]
    if scr[i] <low:
        low=scr[i]
a=total/p
print(a)
print(high)
print(low)
print(total)