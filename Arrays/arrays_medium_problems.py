# Array medium problems or you can say Level tWo problems in array


# Duplicate within K Distance in an Array
# Given an integer array arr[] and an integer k, determine whether there exist two indices i and j such that arr[i] == arr[j] and |i - j| ≤ k. 
#If such a pair exists, return 'Yes', otherwise return 'No'.
# Input: k = 3, arr[] = [1, 2, 3, 1, 4, 5]--> Output: Yes
class SOlution:
    def duplicate_within_k_distance(self, arr, k):
        last_seen = {}
        for i, num in enumerate(arr):
            if num in last_seen:
                if i - last_seen[num] <= k:
                    return "yes"
            last_seen[num] = i
        return "No"
s = SOlution()
arr = [1, 2, 3, 1, 4, 5]
print(s.duplicate_within_k_distance(arr, 3))


# Rearrange array such that even positioned are greater than odd
# Given an array arr[], rearrange its elements according to 1-based indexing such that for every even index i, arr[i] is greater than or equal to arr[i-1],
# and for every odd index i, arr[i] is less than or equal to arr[i-1]. Return the rearranged array that satisfies these conditions for all valid indices.
# Find the resultant array.[consider 1-based indexing].
# Input: arr[] = [1, 2, 2, 1]  ->  Output: [2 1 2 1]
class Solution:
    def rearrange_arr(self, arr):   # Alternative sorting  problem
        for i in range(1, len(arr)):
            if (1 + i) % 2 == 0:
                if arr[i] > arr[i-1]:
                    arr[i] , arr[i-1] = arr[i-1], arr[i]
            else:
                if arr[i] < arr[i-1]:
                    arr[i], arr[i-1] = arr[i-1], arr[i]
        return arr
s = Solution()
arr = [1, 2, 2, 1] 
print(s.rearrange_arr(arr))  



# # Sum of all Subarrays
# Given an integer array arr[], compute the sum of all possible sub-arrays of the array. A sub-array is a contiguous part of the array.
# Input: arr[] = [1, 4, 5, 3, 2] ->> Output: 116
class Solution:
    def sum_of_all_subarrays(self, arr):
        subarrays = []
        for i in range(len(arr)):
            for j in range(i, len(arr)):
                subarrays.append(arr[i:j+1])
        return subarrays

s = Solution()
arr = [1, 3, 2]
print(s.sum_of_all_subarrays(arr))


# # Find Smallest Missing Positive Number
# Given an unsorted array arr[] with both positive and negative elements, the task is to find the smallest positive number missing from the array.
# Note: You can modify the original array.
# Input: arr[] = {2, -3, 4, 1, 1, 7} -->> Output: 3
# Explanation: 3 is the smallest positive number missing from the array.
class Solution:
    def smallest_missing_number(self, arr):
        new_set = set()
        for num in arr:
            if num not in new_set:
                new_set.add(num)

        i = 1
        while True:
            if i not in new_set:
                return i
            i += 1
s = Solution()
arr = [2, -3, 4, 1, 1, 7]
print(s.smallest_missing_number(arr))


# Stock Buy and Sell - Multiple Transaction Allowed
# Given an array prices[] representing stock prices, find the maximum total profit that can be earned by buying and selling the stock any number of times.
# Note: We can only sell a stock which we have bought earlier and we cannot hold multiple stocks on any day.
# Input: prices[] = [100, 180, 260, 310, 40, 535, 695]  --> Output: 865
class Solution:
    def max_profit(Self, arr):
        profit = 0
        for i in range(1, len(arr)):
            if arr[i] > arr[i-1]:
                profit += arr[i] - arr[i-1]
        return profit

s = Solution()
arr = [100, 180, 260, 310, 40, 535, 695]
print(s.max_profit(arr))


# Stock Buy and Sell - Max one Transaction Allowed
# Given an array prices[] of non-negative integers, representing the prices of the stocks on different days, find the maximum profit possible by buying 
# and selling the stocks on different days when at most one transaction is allowed. Here one transaction means 1 buy + 1 Sell. 
# If it is not possible to make a profit then return 0.
# Note: Stock must be bought before being sold.
# Input: prices[] = [7, 10, 1, 3, 6, 9, 2] -- > Output: 8
class Solution:
    def stock_buy_sell(self, prices):
        min_price = prices[0]
        max_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit
        return max_profit
s = Solution()
arr = [7, 10, 1, 3, 6, 9, 2]
print(s.stock_buy_sell(arr))


# Majority Element
# Given an array arr[] of size n, find the element that appears more than ⌊n/3⌋ times. If no such element exists, return -1.
# Input: arr[] = [1, 1, 2, 1, 3, 5, 1] --> Output: 1
class Solution:
    def majority_element(self, arr, n):
        element1 = element2 = None
        count1 = count2 = 0
        for num in arr:
            if element1 == num:
                count1 += 1
            elif element2 == num:
                count2 += 1
            elif count1 == 0:
                element1 = num
                count1 = 1
            elif count2 == 0:
                element2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        result = []
        n = len(arr)
        for element in [element1, element2]:
            if element is not None and arr.count(element) > n//3:
                result.append(element)
        return result
s = Solution()
arr = [1, 1, 2, 1, 3, 5, 1]
print(s.majority_element(arr, 3))

# Majority Element
# Given an array arr[] of size n, find the element that appears more than ⌊n/2⌋ times. If no such element exists, return -1.
# Input: arr[] = [1, 1, 2, 1, 3, 5, 1] --> Output: 1
class Solution:
    def majority_ele(self, arr, n):
        element1 = None
        count1 = 0
        for num in arr:
            if element1 == num:
                count1 += 1
            elif count1 == 0:
                element1 = num
                count1 = 1
            else:
                count1 -= 1
        result = []
        n = len(arr)
        if element1 is not None and arr.count(element1) > n // 2 :
            result.append(element1)
        return result
s = Solution()
arr = [1, 1, 2, 1, 3, 5, 1]
print(s.majority_ele(arr, 2))


# Maximum Subarray Sum - Kadane's Algorithm
# Given an integer array arr[], find the subarray (containing at least one element) which has the maximum possible sum, and return that sum.
class Solution:
    def max_subarray_sum(self, arr):
        max_so_far = arr[0]
        current_sum = arr[0]
        for i in range(1, len(arr)):
            current_sum = max(arr[i], current_sum + arr[i])
            max_so_far = max(max_so_far, current_sum)
        return f"Maximum Subarray Sum: {max_so_far}"
s = Solution()
arr = [2, 3, -8, 7, -1, 2, 3]
print(s.max_subarray_sum(arr))


# MAximum Subarray product - "Kadanes Algorithm"
class Solution:
    def max_subarr_product(self, arr):
        max_product = arr[0]
        min_product = arr[0]
        result = arr[0]
        for i in range(1, len(arr)):
            if arr[i] < 0:
                   max_product, min_product = min_product, max_product
            max_product = max(arr[i], max_product * arr[i])
            min_product = min(arr[i], min_product*arr[i])
            result = max(result, max_product)
        return f"Maximum subarray Product: {result}"
s = Solution()
arr = [2, 3, -2, 4]
print(s.max_subarr_product(arr))


        