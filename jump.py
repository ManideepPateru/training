L=list(map(int,input().split()))
def game(L):
    max_reach=0
    for i in range(len(L)):
        if(i>max_reach):
            return False
        else:
            max_reach=max(max_reach,i+L[i])
    return True
print(game(L))