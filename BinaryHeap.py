import numpy as np
import math
from Interfaces import Queue
from Interfaces import Tree

def left(i: int) -> int:
    """
    helper method; returns the index of the left child of the element at index i
    """
    return 2 * i + 1

def right(i: int) -> int:
    """
    helper method; returns the index of the right child of the element at index i
    """
    return 2 * (i + 1)


def parent(i: int) -> int:
    """
    helper method; returns the index of the parent of the element at index i
    """
    return math.floor((i - 1) / 2)


def _new_array(n: int) -> np.array:
    """
    helper method; creates a new numpy array of 0's of size n
    """
    return np.zeros(n, object)


class BinaryHeap(Queue, Tree):
    def __init__(self):
        self.a = _new_array(1)
        self.n = 0

    def add(self, x: object):
        if len(self.a) == self.n:
            self._resize()
        self.a[self.n] = x
        self.n += 1
        self._bubble_up_last()
        return True

    def remove(self):
        if self.n == 0: raise IndexError()
        x = self.a[0]
        self.a[0] = self.a[self.n - 1]
        self.n -= 1
        self._trickle_down_root()
        if 3 * self.n < len(self.a):
            self._resize()
        return x

    def depth(self, u) -> int:
        for i in range(self.n):
            if self.a[i] == u:
                return math.floor(math.log2(i + 1))
        raise ValueError(f"{u} is not found in the binary tree.")

    def height(self) -> int:
        if self.n == 0: return -1
        return math.floor(math.log2(self.n))

    def bf_order(self) -> list:
        return list(self.a[0:self.n])

    def in_order(self) -> list:
        result = []
        self._in_order(0, result)
        return result
    
    def _in_order(self, i, result):
        if i < self.n:
            self._in_order(left(i), result)
            result.append(self.a[i])
            self._in_order(right(i), result)

    def post_order(self) -> list:
        result = []
        self._post_order(0, result)
        return result
    
    def _post_order(self, i, result):
        if i < self.n:
            self._post_order(left(i), result)
            self._post_order(right(i), result)
            result.append(self.a[i])
            
    def pre_order(self) -> list:
        result = []
        self._pre_order(0, result)
        return result
    
    def _pre_order(self, i, result):
        if i < self.n:
            result.append(self.a[i])
            self._pre_order(left(i), result)
            self._pre_order(right(i), result)

    def size(self) -> int:
        return self.n

    def find_min(self):
        if self.n == 0: raise IndexError()
        return self.a[0]

    def _bubble_up_last(self):
        i = self.n - 1
        p_idx = parent(i)
        while i > 0 and self.a[i] < self.a[p_idx]:
            self.a[i], self.a[p_idx] = self.a[p_idx], self.a[i]
            i = p_idx
            p_idx = parent(i)

    def _resize(self):
        b = _new_array(max(1, 2 * self.n))
        for i in range(self.n):
            b[i] = self.a[i]
        self.a = b

    def _trickle_down_root(self):
        i = 0
        while True:
            l_idx = left(i)
            r_idx = right(i)
            min_idx = i
            if l_idx < self.n and self.a[l_idx] < self.a[min_idx]:
                min_idx = l_idx
            if r_idx < self.n and self.a[r_idx] < self.a[min_idx]:
                min_idx = r_idx
            if min_idx == i:
                break

            self.a[i], self.a[min_idx] = self.a[min_idx], self.a[i]
            i = min_idx
            l_idx = left(i)
            r_idx = right(i)


    def __str__(self):
        return str(self.a[0:self.n])