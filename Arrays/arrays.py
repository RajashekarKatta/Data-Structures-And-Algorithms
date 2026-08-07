# Arrays
# An Array is a collection of similar types of elements stored in a comtigous memory location. we can access the item through array index numbers




# Baic Array Problems
print("__" * 30)

# Alternate elements of an array
class Solution:
    def alter_native_elements(self, arr):
        result = []
        for i in range(0, len(arr), 2):
            result.append(arr[i])
        return result

s = Solution()
arr = [1, 2, 3, 4, 5, 6]
print(s.alter_native_elements(arr))