# Quick Sort
""""QuickSort is a sorting algorithm based on the Divide and Conquer that picks an element as a pivot and partitions the given array around the picked pivot by placing the pivot in its correct position in the sorted array. .

There are mainly three steps in the algorithm:

Choose a Pivot: Select an element from the array as the pivot. The choice of pivot can vary (e.g., first element, last element, random element, or median).
Partition the Array: Re arrange the array around the pivot. After partitioning, all elements smaller than the pivot will be on its left, and all elements greater than the pivot will be on its right.
Recursively Call: Recursively apply the same process to the two partitioned sub-arrays.
Base Case: The recursion stops when there is only one element left in the sub-array, as a single element is already sorted."""

# Quick Sort implementation but we are using extra space O(n)
class Solution:
    def quick_sort(self, arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr)//2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]

        return self.quick_sort(left) + middle + self.quick_sort(right)

s = Solution()
arr = [10, 7, 8, 9, 1, 5]
print(s.quick_sort(arr))


"""In-place Quick Sort with Lomuto partitioning modifies the array directly without allocating extra sublists."""
# Quick Sort Partition Function this function does't take extra space so space complexity is O(1)
class Solution:
    def partition(self, arr, low, high):
        pivot = arr[high]
        i = low -1

        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[high] = arr[high], arr[i+1]
        return i + 1

    def Quick_sort(self, arr, low, high):
        if low < high:
            pivot_index = self.partition(arr, low, high)
            self.Quick_sort(arr, low, pivot_index-1)
            self.Quick_sort(arr, pivot_index + 1, high)

s = Solution()
arr =  [5, 3, 8, 4, 2]
s.Quick_sort(arr, 0, len(arr)-1)
print(arr)


    

# Simple Quick Sort
class Solution:
    def partition(self, arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[j], arr[i] = arr[i], arr[j]
        arr[i+1] , arr[high] = arr[high], arr[i+1]
        return i + 1

    def simple_quick_sort(self, arr, low, high):
        if low < high:
            pivot_index = self.partition(arr, low, high)
            self.simple_quick_sort(arr, low, pivot_index-1)
            self.simple_quick_sort(arr, pivot_index + 1, high)

s = Solution()
arr = [5,3,4,6,7,1,2]
s.simple_quick_sort(arr, 0, len(arr) - 1)
print(arr)