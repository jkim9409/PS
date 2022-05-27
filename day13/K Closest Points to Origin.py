# https://leetcode.com/problems/k-closest-points-to-origin/
# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).
#
# The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).
#
# You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).
#
# Ex1:
# Input: points = [[1,3],[-2,2]], k = 1
# Output: [[-2,2]]
#
# Ex2:
# Input: points = [[3,3],[5,-1],[-2,4]], k = 2
# Output: [[3,3],[-2,4]]

import heapq

def cal_dist(point):
    return point[0] * point[0] + point[1] * point[1]

def k_closest_builtin(points,k):
    dists = []
    heap = []
    for point in points:
        dist = cal_dist(point)
        heapq.heappush(heap, dist)
        dists.append(dist)

    kth_dist = [heapq.heappop(heap) for _ in range(k)][-1]
    return [points[idx] for idx, dist in enumerate(dists) if dist <= kth_dist]

print(k_closest_builtin([[3,3],[5,-1],[-2,4]],2))

def kClosest(points,k):
    heap = []
    for (x,y) in points:
        dist = x**2 + y**2
        heapq.heappush(heap,(dist,x,y))

    result = []
    for _ in range(k):
        (dist,x,y) = heapq.heappop(heap)
        result.append((x,y))
    return result

print(kClosest([[3,3],[5,-1],[-2,4]],2))






class BinaryMinHeap:
    def __init__(self):
        self.items = [None]

    def __len__(self):
        return len(self.items) - 1

    def _percolate_up(self):

        cur = len(self)

        parent = cur//2

        while parent > 0:
            if self.items[cur] < self.items[parent]:
                self.items[cur], self.items[parent] = self.items[parent],self.items[cur]

            cur = parent
            parent = cur//2


    def _percolate_down(self,cur):
        smallest = cur
        left = 2 * cur
        right = 2* cur + 1

        if left <= len(self) and self.items[left] < self.items[smallest]:
            smallest = left
        if right <= len(self) and self.items[right] < self.items[smallest]:
            smallest = right

        if smallest != cur:
            self.items[cur],self.items[smallest] = self.items[smallest],self.items[cur]
            self._percolate_down(smallest)


    def insert(self,dist):
        self.items.append(dist)
        self._percolate_up()

    def _extract(self):
        if len(self) < 1:
            return None

        root = self.items[1]
        self.items[1] = self.items[-1]
        self.items.pop()
        self._percolate_down(1)

        return root


def cal_dist(point):
    return point[0] * point[0] + point[1] * point[1]

def k_closest(points,k):
    heap = BinaryMinHeap()
    dists = []
    for point in points:
        dist =  cal_dist(point)
        heap.insert(dist)
        dists.append(dist)

    kth_dist = [heap._extract() for _ in range(k)][-1]
    return [points[idx] for idx, dist in enumerate(dists) if dist <= kth_dist]

print(k_closest([[3,3],[5,-1],[-2,4]],2))