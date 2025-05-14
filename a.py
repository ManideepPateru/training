n=int(input())
if n%2!=0:
    print("no")
else:
    k=n//2
    if k%2==0:
        print(k,k)
    else:
        print(k-1,k+1)