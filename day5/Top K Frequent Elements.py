# https://leetcode.com/problems/top-k-frequent-elements/
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
# Ex1:
# imput: nums = [1,1,1,2,2,3], k = 2
# output: [1,2]
#
# Ex2:
# input: nums = [1], k = 1
# output: [1]


# my solution using counter
# nums = [1,1,1,2,2,3,3,3,3]
# k = 1
#
# import collections
# a = collections.Counter(nums).most_common(k)
# b = list(zip(*a))[0]
# print(b)



#Textbook solution using heapq
# import collections
# import heapq
#
#
# def topKFrequend (nums,k):
#     freqs = collections.Counter(nums)
#     freqs_heap = []
#
#     for f in freqs:
#         heapq.heappush(freqs_heap,(-freqs[f],f))
#     topk = list()
#
#     for _ in range(k):
#         topk.append(heapq.heappop(freqs_heap)[1])
#
#     return topk
#
# nums = [1,1,1,2,2,3]
# k = 2
#
# print(topKFrequend(nums,k))



# #textbook solution the pythonic way
# import collections
# def topKFrequentpython(nums,k):
#     return list(zip(*collections.Counter(nums).most_common(k)))[0]
#
# nums = [1,1,1,2,2,3]
# k = 2
#
# print(topKFrequentpython(nums,k))