# https://leetcode.com/problems/course-schedule/
# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1.
# You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
# Return true if you can finish all courses. Otherwise, return false.
#
# Ex1:
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
#
# Ex2:
# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false


import collections
def canFinish(numCourses,prerequisites):
    graph = collections.defaultdict(list)
    for x, y in prerequisites:
        graph[x].append(y)

    traced = set()

    def dfs(i):
        if i in traced:
            return False

        traced.add(i)

        for y in graph[i]:
            if not dfs(y):
                return False

        traced.remove(i)

        return True

    for x in list(graph):
        if not dfs(x):
            return False

    return True

numCourses = 2
prerequisites = [[0,1],[0,2],[1,2],[1,3],[3,1]]

print(canFinish(numCourses,prerequisites))

import collections
def canFinish_pruning(numCourses,prerequisites):
    graph = collections.defaultdict(list)
    for x,y in prerequisites:
        graph[x].append(y)

    traced = set()
    visited = set()

    def dfs(i):

        if i in traced:
            return False
        if i in visited:
            return True

        traced.add(i)
        for y in graph[i]:
            if not dfs(y):
                return False

        traced.remove(i)
        visited.add(i)
        return True

    for x in list(graph):
        if not dfs(x):
            return False
    return True
numCourses = 2
prerequisites = [[0,1],[0,2],[1,2],[1,3],[3,1]]

print(canFinish_pruning(numCourses,prerequisites))

