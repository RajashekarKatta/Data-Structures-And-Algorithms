# Quick Sort
# Quick Sort Partition Function
class Solution:
    def partition(self, arr, low, high):
        pivot = arr[high]
        i = low -1
        for j in range(low, high):
            if arr[j] < pivot:
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


