# Merge Sort
"""Merge sort is a popular sorting algorithm known for its efficiency and stability. It follows the Divide and Conquer approach. 
It works by recursively dividing the input array into two halves, recursively sorting the two halves and finally merging them back together to obtain the sorted array."""

"""
Here's a step-by-step explanation of how merge sort works:

Divide: Divide the list or array recursively into two halves until it can no more be divided.
Conquer: Each subarray is sorted individually using the merge sort algorithm.
Merge: The sorted subarrays are merged back together in sorted order. The process continues until all elements from both subarrays have been merged."""

# Merge Sort implementation in Python   this is not in palce progrma we are using external space ex: Sorted_arr this takes extra space so space complexity is O(n) and time is O(nlogn)
class Solution:
    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left_half = self.merge_sort(arr[:mid])
        right_half = self.merge_sort(arr[mid:])

        return self.merge(left_half, right_half)
    
    def merge(self, left, right):
        sorted_arr = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sorted_arr.append(left[i])
                i += 1
            else:
                sorted_arr.append(right[j])
                j += 1

        # Append remaining elements
        sorted_arr.extend(left[i:])
        sorted_arr.extend(right[j:])

        return sorted_arr

s = Solution()
arr = [38, 27, 43, 3, 9, 82, 10]
print(s.merge_sort(arr))




# Merge sort implementing in-place
"""Standard Merge Sort is not truly in-place, because the usual merge step needs an extra temporary array of O(n) space."""
class Solution:
    def merge_sort_in_place(self, arr, low, mid, high):
        i = low
        j = mid + 1
        while i <= mid and j <= high:
            if arr[i] <= arr[j]:
                i += 1
            else:
                value = arr[j]
                index = j
                while index > i:
                    arr[index] = arr[index - 1]
                    index -= 1
                arr[i] = value

                i += 1
                mid += 1
                j += 1

    def merge(self, arr, low, high):
        if low < high:
            mid = (low + high) // 2
            self.merge(arr, low, mid)
            self.merge(arr, mid+1, high)

            self.merge_sort_in_place(arr, low, mid, high)

s = Solution()
arr = [12, 11, 13, 5, 6, 7]
s.merge(arr, 0, len(arr) - 1)
print(arr)



class Solution:
    def merge_sort(self, arr, low, mid, high):
        i = low
        j = mid + 1
        while i <= mid and j <= high:
            if arr[i] <= arr[j]:
                i += 1
            else:
                value = arr[j]
                index = j
                while index > i:
                    arr[index] = arr[index - 1]
                    index -= 1
                arr[i] = value

                i += 1
                mid += 1
                j += 1

    def merge(self, arr, low, high):
        if low < high:
            mid = (low + high) // 2
            self.merge(arr, low, mid)
            self.merge(arr, mid+1, high)

            self.merge_sort(arr, low, mid, high)

s = Solution()
arr = [12, 11, 13, 5, 6, 7]
s.merge(arr, 0, len(arr) - 1)
print(arr)






    
