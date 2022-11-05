class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprice = 0
        l=0
        r = l+1
        while r < len(prices):
            if prices[l] > prices[r]:
                l+=1
                r=l+1
            else:
                maxprice=max(maxprice, prices[r]-prices[l])
                r+=1
        return maxprice