s=[]
for _ in range(int(input())): # повторения кол-во
    n=int(input())# длинуля
    b =[int(x) for x in input()]
    s.append([str(b[n-1]) for _ in range(n)])


for i in s:
    print(''.join(i))
