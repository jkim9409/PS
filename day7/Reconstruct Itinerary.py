# https://leetcode.com/problems/reconstruct-itinerary/
# You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it.
#
# All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string.
# You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once
#
# Ex1:
# Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
# Output: ["JFK","MUC","LHR","SFO","SJC"]

# Ex2:
# Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
#

import collections


# def findItinerary_dfs(tickets):
#     graph = collections.defaultdict(list)
#     for a,b in sorted(tickets):
#         graph[a].append(b)
#
#     route = []
#     def dfs(a):
#         while graph[a]:
#             dfs(graph[a].pop(0))
#         route.append(a)
#     dfs("JFK")
#     return route[::-1]
#
#
#
#
# tickets1 = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
# tickets2 = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
#
#
#
# print(findItinerary_dfs(tickets1))
# print(findItinerary_dfs(tickets2))

# def findItinerary_stack(tickets):
#     graph = collections.defaultdict(list)
#     for a,b in sorted(tickets,reverse = True):
#         graph[a].append(b)
#
#     route = []
#
#     def dfs(a):
#         while graph[a]:
#             dfs(graph[a].pop())
#         route.append(a)
#     dfs("JFK")
#     return route[::-1]
#
#
#
# tickets1 = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
# tickets2 = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
# print(findItinerary_stack(tickets1))
# print(findItinerary_stack(tickets2))


def findItinerary_stackonly(tickets):
    graph = collections.defaultdict(list)
    for a,b in tickets:
        graph[a].append(b)

    route = []
    stack = ['JFK']
    while stack:
        while graph[stack[-1]]:
            stack.append(graph[stack[-1]].pop(0))
        route.append(stack.pop())

    return route[::-1]


tickets1 = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
tickets2 = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
print(findItinerary_stackonly(tickets1))
print(findItinerary_stackonly(tickets2))