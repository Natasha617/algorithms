n = [int(input()) for _ in range(int(input()))]
for i in n:
    flag = True
    if i == 1:
      flag = False
    j = 2
    flag = True
    while j*j<=i:
      if i%j==0:
        flag = False
        break
      j+=1
    if flag:
      print('Yes')
    else:
      print('NO')
