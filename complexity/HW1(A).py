t=int(input())
k = [1,2,3,4,5,6,7,8,9,10]
answ=[]
for _ in range(t):
    ab=input()
    a,b = int(ab.split(" ")[0]),int(ab.split(" ")[1])
    if a!=b:
        d = abs(b-a)
        if d in k:
            answ.append(1)
        else:
            answ.append(d//10 if d %10 ==0 else d//10+1)
    else:
        answ.append(0)
print(*answ,sep='\n')
