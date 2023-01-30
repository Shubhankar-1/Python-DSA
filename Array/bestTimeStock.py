class Solution:
    def maxProfit(prices):
        min_price = prices[0]
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
                print("min_price - ", min_price)
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
                print("max_price - ", max_profit)

        return max_profit

        # max = 0
        # for x in range(len(prices)):
        #     for y in range(x+1, len(prices)):
        #         if prices[x] < prices[y]:
        #             z = abs(prices[x]-prices[y])
        #             if z > max:
        #                 max = z

        # return max


if __name__ == '__main__':
    a = Solution
    print(a.maxProfit(prices=[7, 1, 5, 3, 6, 0]))
