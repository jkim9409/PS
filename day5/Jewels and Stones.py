# https://leetcode.com/problems/jewels-and-stones/
# You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have.' \
#    ' Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.
#
# Letters are case sensitive, so "a" is considered a different type of stone from "A".
#
#
# Ex1:
# input: jewels = "aA", stones = "aAAbbbb"
# output: 3
#
# Ex2:
# input: jewels = "z", stones = "ZZ"
# output: 0


# my solution

# import collections
# jewels = "z"
# stones = "ZZ"
# counter = collections.Counter(stones)
# sum = 0
# for char in jewels:
#     if char in counter:
#         sum += counter[char]
# print(sum)


#Using Hash Table
# def newJewelsInStones_solution1(j,s):
# using hash table when you GET the data, it is much faster O(1)

#     freqs = {}
#     count = 0
#
#     for char in s:
#         if char not in freqs:
#            freqs[char] = 1
#
#         else:
#             freqs[char] +=1
#
#     for char in j:
#         if char in freqs:
#             count+=freqs[char]
#
#     return count
#
#
# s1 = "aAAbbbb"
# j1 = "aA"
# s2 = "ZZ"
# j2 = "z"
# print(newJewelsInStones_solution1(j1,s1))
# print(newJewelsInStones_solution1(j2,s2))


#using defaultdict ( won't give error with unmatching key)

# import collections
# def newJewelsInStones_solution2 (j,s):
#     freqs = collections.defaultdict(int)
#     count = 0
#
#     for char in s:
#         freqs[char] += 1 # we don't need "if statement" bc of default dict
#
#     for char in j:
#         count += freqs[char] # we don't need "if statement" bc of default dict
#
#     return count
#
# s1 = "aAAbbbb"
# j1 = "aA"
# s2 = "ZZ"
# j2 = "z"
# print(newJewelsInStones_solution2(j1,s1))
# print(newJewelsInStones_solution2(j2,s2))


#soulution using counter

# import collections
# def newJewelsInStones_solution3 (j,s):
#     freqs = collections.Counter(s)
#     count = 0
#     for char in j:
#         count += freqs[char]
#
#     return count
#
# s1 = "aAAbbbb"
# j1 = "aA"
# s2 = "ZZ"
# j2 = "z"
# print(newJewelsInStones_solution3(j1,s1))
# print(newJewelsInStones_solution3(j2,s2))




# most pythonic way
#
# def newJewelsInStones_solution4(j,s):
#     return sum(char in j for char in s) #List comprehension sum([char in j for char in s])
#
# s1 = "aAAbbbb"
# j1 = "aA"
# s2 = "ZZ"
# j2 = "z"
# print(newJewelsInStones_solution4(j1,s1))
# print(newJewelsInStones_solution4(j2,s2))

