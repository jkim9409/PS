# class BinaryMaxHeap:
#     def __init__(self):
#         # 계산 편의를 위해 0 이 아닌 1번째 인덱스부터 사용할 것이다.
#         self.items = [None]
#
#     def __len__(self):
#         # len() 연산을 하늫하게 하는 매직 메서드 덮어쓰기이다 (Override).
#         return len(self.items) - 1
#
#     def _percolate_up(self):
#         # percolate: 스며들다
#         cur = len(self)
#         # left 라면 2*cur, right 이라면 2*cur + 1 의 인덱스를 가지므로 parent 는 항상 cur//2 로 표현할수 있다.
#         parent = cur // 2
#
#         # while 문을 통해 부모보다 큰 값을 가지고 있는 노드를 계속 올려준다
#         while parent > 0:
#             if self.items[cur] > self.items[parent]:
#                 self.items[cur], self.items[parent] = self.items[parent], self.items[cur]
#
#             cur = parent
#             parent = cur // 2
#
#     def _percolate_down(self, cur):
#         biggest = cur
#         left = 2 * cur
#         right = 2 * cur + 1
#
#         # 부모노드와 왼쪽 오른쪽 값을 비교해서 계속 아래로 내려보낸다.
#         if left <= len(self) and self.items[left] > self.items[right]:
#             biggest = left
#         if right <= len(self) and self.items[right] > self.items[left]:
#             biggest = right
#         if biggest != cur:
#             self.items[cur], self.items[biggest] = self.items[biggest],self.items[cur]
#             self._percolate_down(biggest)
#
#     def insert(self,k):
#         self.items.append(k)
#         self._percolate_up()
#     def extract(self):
#         if len(self) < 1:
#             return None
#
#         root = self.items[1]
#         self.items[1] = self.items[-1]
#         self.items.pop()
#         self._percolate_down(1)
#
#         return root

class BinaryMaxHeap:
    def __init__(self):
        # 계산 편의를 위해 0이 아닌 1번째 인덱스부터 사용한다.
        self.items = [None]

    def __len__(self):
        # len() 연산을 가능하게 하는 매직 메서드 덮어쓰기(Override).
        return len(self.items) - 1

    def _percolate_up(self):
        # percolate: 스며들다.
        cur = len(self)
        # left 라면 2*cur, right 라면 2*cur + 1 이므로 parent 는 항상 cur // 2
        parent = cur // 2

        while parent > 0:
            if self.items[cur] > self.items[parent]:
                self.items[cur], self.items[parent] = self.items[parent], self.items[cur]

            cur = parent
            parent = cur // 2

    def _percolate_down(self, cur):
        biggest = cur
        left = 2 * cur
        right = 2 * cur + 1

        if left <= len(self) and self.items[left] > self.items[biggest]:
            biggest = left

        if right <= len(self) and self.items[right] > self.items[biggest]:
            biggest = right

        if biggest != cur:
            self.items[cur], self.items[biggest] = self.items[biggest], self.items[cur]
            self._percolate_down(biggest)

    def insert(self, k):
        self.items.append(k)
        self._percolate_up()

    def extract(self):
        if len(self) < 1:
            return None

        root = self.items[1]
        self.items[1] = self.items[-1]
        self.items.pop()
        self._percolate_down(1)

        return root


def test_maxheap_we_made(lst,k):
    maxheap = BinaryMaxHeap()

    for el in lst:
        maxheap.insert(el)

    return [maxheap.extract() for _ in range(k)][k-1]

lst = [3, 2, 3, 1, 2, 4, 5, 5, 6]

print(test_maxheap_we_made(lst,1))