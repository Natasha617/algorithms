s = []
for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    if k%2 !=0:
      d = max(a)
      a = list(map(lambda x: d-x, a))   
    else:
      for _ in range(2):
        d = max(a)
        a = list(map(lambda x: d-x, a))
    s.append(a)
for i in s:
  print(*i) 
