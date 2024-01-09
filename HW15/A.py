n = int(input())
d = []
i=2
while i**2 <= n:
  while n%i == 0:
    d.append(i)
    n //= i
  i += 1
if n>1:
  d.append(n) 
print(*d)
