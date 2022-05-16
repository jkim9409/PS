# https://leetcode.com/problems/remove-duplicate-letters/
# Given a string s, remove duplicate letters so that every letter appears once and only once.
# You must make sure your result is the smallest in lexicographical order among all possible results.
#
# Ex1:
# input:s = "bcabc"
# output: "abc"
#
# Ex2:
# input: s = "cbacdcbc"
# output: "acdb"
#

# ------------------------------------------------------------------------------------------
import collections


def removeDuplicateLetters_recursive(s):
    for char in sorted(set(s)):
        suffix = s[s.index(char):]
        if set(s) == set(suffix):
            return char + removeDuplicateLetters_recursive(suffix.replace(char,''))
    return ''

def removeDuplicateLetters_list(s):
    counter, stack = collections.Counter(s),[]

    for char in s:
        counter[char] -= 1

        if char in stack:
            continue
        while stack and char < stack[-1] and counter[stack[-1]] > 0:
            stack.pop()

        stack.append(char)

    return ''.join(stack)

def removeDuplicateLetters_stack(s):
    counter, seen, stack = collections.Counter(s),set(),[]

    for char in s:
        counter[char] -= 1
        if char in seen:
            continue
        while stack and char < stack[-1] and counter[stack[-1]] >0:
            seen.remove(stack.pop())
        stack.append(char)
        seen.add(char)
    return ''.join(stack)


print(removeDuplicateLetters_stack('dbcdacbebc'))