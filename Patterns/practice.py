class Solution:
    def smallest_subarray(self, arr, k):
        left = 0
        current_sum = 0
        min_length = float('inf')
        result = []
        for right in range(len(arr)):
            current_sum += arr[right]
            while current_sum >= k:
                if min_length > (right- left + 1):
                    min_length = right - left + 1
                    result = arr[left:right+1]
                current_sum -= arr[left]
                left += 1
        return result

a = Solution()
arr = [2, 3, 1, 2, 4, 3]
print(a.smallest_subarray(arr, 7))