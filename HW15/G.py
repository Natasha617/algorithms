def is_not_prime(n):
    if n == 1:
        return True
    i = 2
    while i * i <= n:
        if n % i == 0:
            return True
        i += 1
    return False
a,b = map(int,input().split())
lst = [i for i in range(a,b+1)]

for i in range(len(lst)): # можно и до sqrt(N)
    if lst[i] and is_not_prime(lst[i]):
      lst[i]=0
d = []   
for i in range(len(lst)):
    if lst[i]:
        d.append(lst[i])
print(*d)
