# Array medium problems or you can say Level tWo problems in array


# Duplicate within K Distance in an Array
# Given an integer array arr[] and an integer k, determine whether there exist two indices i and j such that arr[i] == arr[j] and |i - j| ≤ k. 
#If such a pair exists, return 'Yes', otherwise return 'No'.
# Input: k = 3, arr[] = [1, 2, 3, 1, 4, 5]--> Output: Yes
from django.conf.locale import ar


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



# Given an array of integers, every element in the array appears twice except for one element which appears only once. 
# The task is to identify and return the element that occurs only once. 
# Input:  arr[] = [2, 3, 5, 4, 5, 3, 4]  --> # Output: 2 
class Solution:
    def unique_number(self, arr):
        hash_map = {}
        for num in arr:
            hash_map[num] = hash_map.get(num, 0) + 1
        for num in hash_map:
            if hash_map[num] == 1:
                return num

s = Solution()
arr = [2,3,5,4,5,3,4]
print(s.unique_number(arr))  


# Equilibrium Index
# Given an array arr[] of size n, the task is to return an equilibrium index (if any) or -1 if no equilibrium index exists. 
# The equilibrium index of an array is an index such that the sum of all elements at lower indexes equals the sum of all elements at higher indexes.
# ఈక్విలిబ్రియం ఇండెక్స్ (Equilibrium Index) అంటే ఒక అర్రే (array) లోని ఒక నిర్దిష్ట స్థానం (index). ఆ స్థానానికి ఎడమ వైపు (left side) ఉన్న సంఖ్యల మొత్తం 
#(sum) మరియు కుడి వైపు (right side) ఉన్న సంఖ్యల మొత్తం సరిసమానంగా ఉంటే, ఆ ఇండెక్స్‌ను "Equilibrium Index" అంటారు
# nput: arr[] = [1, 2, 0, 3]  --> Output: 2
class Solution:
    def equilibrium_index(self, arr):
        left_sum = 0
        total_sum = sum(arr)
        for i in range(len(arr)):
            right_sum = total_sum - arr[i] - left_sum
            if left_sum == right_sum:
                return f"Equilibrium index is {i}"
            left_sum += arr[i]
        return f"No equilibrium index found"

s = Solution()
arr = [1, 2, 0, 3]
print(s.equilibrium_index(arr))



# Missing and Repeating in an Array
# Given an unsorted array arr[] of size n, containing elements from the range 1 to n, it is known that one number in this range is missing, 
# and another number occurs twice in the array, find both the duplicate number and the missing number.
class Solution:
    def missing_two_numbers(self, arr):
        n = len(arr)
        freq = [0] * (n+1)
        for num in arr:
            freq[num] += 1
        missing = repeating = -1
        for i in range(1, n+1):
            if freq[i] == 0:
                missing = i
            if freq[i] == 2:
                repeating = i
        return f"Missing number is {missing} and Repeating number is {repeating}"
s = Solution()
arr = [4, 3, 6, 2, 1, 1]
print(s.missing_two_numbers(arr))



# pair of elements with difference k
# Given an array of integers and a target difference $k$, you need to find if there exists a pair of elements in the array whose absolute difference is 
# exactly k.If such a pair exists, return or print the pair.
# Input: Array = [5, 20, 3, 2, 50, 80], $k = 18
# Output: (2, 20) because $|2 - 20| = 18.
class Solution:
    def closest_pair(self, arr, k):
        n = len(arr)
        arr.sort()
        left, right = 0, 1
        while left < n and right < n:
            diff = arr[right] - arr[left]
            if diff == k:
                return arr[left], arr[right]
            elif diff < k:
                right += 1
            else:
                left += 1
                if left == right:
                    right += 1
        return "No such pair exists"
s = Solution()
arr = [5, 20, 3, 2, 50, 80]
k = 18
print(s.closest_pair(arr, k))


# Merge two sorted arrays
# Given two sorted arrays arr1[] of size n and arr2[] of size m. Merge these two arrays.
# After the merge, the first n smallest elements of the combined sorted array should be stored in arr1[], and the remaining m largest elements should be 
# stored in arr2[]. After the merging process, both arr1[] and arr2[] must remain sorted in non-decreasing order.
# Input: arr1[] = [1, 3, 4, 5], arr2[] = [2, 4, 6, 8] 
# Output: arr1[] = [1, 2, 3, 4], arr2[] = [4 5, 6, 8]
class Solution:
    def merge_sorted_arrays(self, arr1, arr2):
        result = []
        i, j = 0, 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                result.append(arr1[i])
                i += 1
            else:
                result.append(arr2[j])
                j += 1
        while i < len(arr1):
            result.append(arr1[i])
            i += 1
        while j < len(arr2):
            result.append(arr2[j])
            j += 1
        for i in range(len(arr1)):
            arr[i] = result[i]

        for j in range(len(arr2)):
            arr[j] = result[len(arr1) + j]

        return arr1, arr2

s = Solution()
arr1 = [1, 3, 4, 5]
arr2 = [2, 4, 6, 8]
print(s.merge_sorted_arrays(arr1, arr2))