s=[]
for _ in range(int(input())):
    n=int(input())
    d = {} 
    for _ in range(n):
      a=input()
      for el in a:
        if el in d.keys():
          d[el]+=1
        else:
          d[el] = 1
    flag = True
    for el in d.values():
      if el % n !=0:
        flag = False 
    if flag:
        s.append('YES')
    else:
      s.append('NO')
print(*s, sep = '\n')
