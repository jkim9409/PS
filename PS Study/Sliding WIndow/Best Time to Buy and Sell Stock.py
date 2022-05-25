# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
#
# Ex1:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
#
# Ex2:
# Input: prices = [7,6,4,3,1]
# Output: 0
#
# Ex3:
# Input: prices = [2,6,5,3,1,4,7,5]
# Output: 6
#
# Ex4:
# Input: prices = [2,6,5,3,1,4]
# Output: 4

def sellstock_solution1(prices):
    profit = start = 0
    for i,price in enumerate(prices):
        if prices[start] > prices[i]:
            start = i
        else:
            profit = max(profit,prices[i]-prices[start])

    return profit
print(sellstock_solution1([2,6,5,3,1,4]))



# def sellstock_solution2(prices):
#     profit = start = 0
#     result = []
#     for i,price in enumerate(prices):
#         if prices[start] > prices[i]:
#             start = i
#         else:
#             if profit < (prices[i] - prices[start]):
#                 result = [prices[start],prices[i]]
#                 profit = prices[i] - prices[start]
#
#
#     return profit,result
# print(sellstock_solution2([2,6,5,3,1,4,7,5]))
