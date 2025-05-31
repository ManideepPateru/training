class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left=min(weights)
        right=sum(weights)
        def cando(w):
            res=0
            count=1
            for i in weights:
                if res+i<=w:
                    res+=i
                else:
                    res=i
                    count+=1
            return count<=days
        while(left<=right):
            mid=(left+right)//2
            if cando(mid):
                right=mid-1
            else:
                left=mid+1
        return left
                    