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


print("\n\n\n")



# # Leaders in an array
# Given an array arr[] of size n, the task is to find all the Leaders in the array. An element is a Leader if it is greater than or equal to all the elements to its right side.
# Note: The rightmost element is always a leader.
# Input: arr[] = [16, 17, 4, 3, 5, 2]
# Output: [17 5 2]

class Solution:
    def leaders(self, arr):
        leaders = []
        max_from_right = arr[-1]
        leaders.append(max_from_right)
        for num in arr:
            if num > max_from_right:
                max_from_right = num
                leaders.append(num)
        leaders.reverse()
        return leaders

s = Solution()
arr = [16, 17, 4, 3, 5, 2]
print(s.leaders(arr))


print("\n\n\n")



