def maxProfit(prices):
    maxProfit = 0
    minPrice = prices[0]
    
    for i in range(1, len(prices)):
        minPrice = min(minPrice, prices[i])
        profit = prices[i] - minPrice
        maxProfit = max(profit , maxProfit)
    return maxProfit

prices = [7,1,5,3,6,4]
print(maxProfit(prices))
