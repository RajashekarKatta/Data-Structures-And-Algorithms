# Basic String Problems

# Find the length of the given string
class Solution:
    def length_of_string(self, s):
        length = 0
        for char in s:
            length += 1
        return length
a = Solution()
print(a.length_of_string("rajashekar"))



# Check if two strings are same
class Solution:
    def are_strings_equal(self, s1, s2):
        if len(s1) != len(s2):
            return False
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                return False
        return True

a = Solution()
print(a.are_strings_equal("hello", "hello"))



# Program to Search a Character in a String
class Solution:
    def findchar(self, s, ch):
        for i in range(len(s)):
            if s[i] == ch:
                return i
        return -1

a = Solution()
print(a.findchar("geeksforgeeks", "k"))


# Insert a character in String at a Given Position
class Solution:
    def insertchar(self, s ,ch, pos):
        result =''
        for i in range(len(s)):
            if i == pos:
                result += ch
            result += s[i]
        return result
a = Solution()
print(a.insertchar("Geeks", "A", 3))


# Remove a Character from a Given Position
class Solution:
    def remove_char(self, s, pos):
        result = ''
        for i in range(len(s)):
            if i == pos:
                continue
            result += s[i]
        return result

a = Solution()
print(a.remove_char("Geeks", 3))


# Remove all occurrences of a character in a string
class Solution:
    def remove_all_occurrencce(self, s, ch):
        result = ''
        for i in range(len(s)):
            if s[i] == ch:
                continue
            result += s[i]
        return result
a = Solution()
print(a.remove_all_occurrencce("GeeksforGeeks", 'e'))


# Concatenation of Two Strings
class Solution:
    def concatination(self, s1, s2):
        result = ''
        for char in s1:       # Simply you can use "return s1 + s2"
            result += char

        for char in s2:
            result += char
        return result

a = Solution()
print(a.concatination("Hello", "World!"))


# Reverse a String
class Solution:
    def reverse_string(self, s):
        s = list(s)
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return ''.join(s)
a = Solution()
print(a.reverse_string("rajashekar"))


# All substrings of a given String
class Solution:
    def generate_substrings(self, s):
        result =[]
        for i in range(len(s)):
            for j in range(i, len(s)):
                result.append(s[i:j+1])
        return result
a = Solution()
print(a.generate_substrings("abc"))


# Check for Binary String
class Solution:
    def check_binary(self, s):
        for i in range(len(s)):
            if s[i] != '0' and s[i] != '1':
                return False
        return True
a = Solution()
print(a.check_binary("01010101010"))


# Camel case of a given sentence
class Solution:
    def camel_case(self, s):
        words = s.split()
        result = [words[0].lower()]
        for word in words[1:]:
            result.append(word.capitalize())
        return ''.join(result)
a = Solution()
print(a.camel_case("i got intern in geeksforgeeks"))


