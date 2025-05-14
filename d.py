n, m = map(int, input().split())
if n==1:
    print(1)
elif n%m==0:
    print(n//m)
else:
    print((n//m)+(n%m))
        
    
    
    