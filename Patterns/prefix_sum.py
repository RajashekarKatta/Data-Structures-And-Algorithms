# Running sum of 1D array
class Solution:
    def running_sum(self, arr):
        result = []
        total = 0
        for num in arr:
            total += num
            result.append(total)
        return result
s = Solution()
arr = [1,2,3,4]
print(s.running_sum(arr))




