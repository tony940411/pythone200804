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
    scr.append(s)
for i in range(p):
    total=total+int(scr(p))
    if int(scr(p)) > high:
        high=int(scr(p))
    if int(scr(p)) <low
        iow=int(scr(p))
a=total/p
print("總和是"total)
print("平均是"a)
print("最高分數是"high)
print("最低分數是"low)
