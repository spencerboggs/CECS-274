"""An implementation of the adjacency list representation of a graph"""
from Interfaces import Graph, List
import numpy as np
import copy
import ArrayList
import ArrayStack
import ArrayQueue


class AdjacencyList(Graph):

  def __init__(self, n: int):
    self.n = n
    self.adj = np.zeros(n, dtype=ArrayList.ArrayList)
    for i in range(self.n):
      self.adj[i] = ArrayList.ArrayList()

  def size(self) -> int:
    return self.n

  def add_edge(self, i: int, j: int):
    if i < 0 or j < 0 or i >= self.n or j >= self.n:
      raise ValueError()
    if not self.has_edge(i, j):
      self.adj[i].append(j)

  def remove_edge(self, i: int, j: int):
    if i < 0 or j < 0 or i >= self.n or j >= self.n:
      raise ValueError()
    for k in range(self.adj[i].size()):
      if self.adj[i].get(k) == j:
        self.adj[i].remove(k)
        return True
    return False

  def has_edge(self, i: int, j: int) -> bool:
    if i < 0 or j < 0 or i >= self.n or j >= self.n:
      raise ValueError()
    for k in range(self.adj[i].size()):
      if self.adj[i].get(k) == j:
        return True
    return False

  def out_edges(self, i) -> List:
    if i < 0 or i >= self.n:
      raise ValueError()
    return self.adj[i]

  def in_edges(self, i) -> List:
    if i < 0 or i >= self.n:
      raise ValueError()
    temp = []
    for j in range(self.n):
      if self.has_edge(j, i):
        temp.append(j)
    return temp

  def bfs(self, r: int):
    if r < 0 or r >= self.n:
      raise ValueError()
    
    array = ArrayList.ArrayList()
    array.append(r)
    queue = ArrayQueue.ArrayQueue()
    queue.add(r)

    while not queue.n == 0:
      v = queue.remove()
      for i in self.out_edges(v):
        if i not in array:
          array.append(i)
          queue.add(i)

    return array

  def dfs(self, r: int):
    if r < 0 or r >= self.n:
      raise ValueError()
    
    array = []
    stack = [r]

    while len(stack) > 0:
      v = stack.pop()
      if v not in array:
        array.append(v)
        for j in self.out_edges(v)[::-1]:
          if j not in array:
            stack.append(j)

    return array

  def __str__(self):
    s = ""
    for i in range(0, self.n):
      s += "%i:  %r\n" % (i, self.adj[i].__str__())
    return s

  def __str__(self):
    s = ""
    for i in range(0, self.n):
      s += "%i,%r\n" % (i, self.adj[i].__str__())
    return s
