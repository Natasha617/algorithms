s=[]
for _ in range(int(input())):
    n=int(input())
    a=[int(i) for i in input().split(' ')]
    if a[0]+a[1]<=a[-1]:
        s.append([1,2,n])
    else:
        s.append([-1])
for i in s:
    print(*i)
