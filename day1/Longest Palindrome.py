# Example 1:
# input:
# s = "abccccdd"
# output:
# 7
#
# Example 2:
# input:
# s = "a"
# output:
# 1
#
# Example 3:
# input:
# s = "bb"
# output:
# 2

# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
#
# Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

def longestPalindrome_booksolution(s:str) -> str:
    def expand(left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -=1
            right +=1
        return s[left + 1:right]

    if len(s) < 2 or s == s[::-1]:
        return s
    result = ''

    for i in range(len(s) - 1):
        result = max(result,expand(i, i + 1), expand(1, i + 2), key =len)

    return len(result)


# def longestPalindrome_leetcode(s:str) -> int:
#     import collections
#     ans = 0
#     for v in collections.Counter(s).itervalues():
#         ans += v/2 * 2
#         if ans % 2 == 0 and v % 2 == 1:
#             ans += 1
#         return ans
# comment: ...




s1 = "abccccdd"
s2 = "a"
s3 = "bb"

print(longestPalindrome_booksolution(s1))
print(longestPalindrome_booksolution(s2))
print(longestPalindrome_booksolution(s3))

# print(longestPalindrome_leetcode(s1))
# print(longestPalindrome_leetcode(s2))
# print(longestPalindrome_leetcode(s3))
