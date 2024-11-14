from Interfaces import Graph, List
import ArrayList
import ArrayQueue
import ArrayStack
import numpy as np

"""An implementation of the adjacency list representation of a graph"""
class AdjacencyMatrix(Graph):

  def __init__(self, n: int):
    self.n = n
    self.adj = np.zeros((self.n, self.n), dtype=int)

  def size(self) -> int:
    return self.n

  def add_edge(self, i: int, j: int):
    if i < 0 or j < 0 or i >= self.n or j >= self.n:
      raise ValueError()
    self.adj[i][j] = True

  def remove_edge(self, i: int, j: int):
    if i < 0 or j < 0 or i >= self.n or j >= self.n:
      raise ValueError()
    if self.adj[i][j] == False:
      return False
    self.adj[i][j] = False
    return True
    
  def has_edge(self, i: int, j: int) -> bool:
    if i < 0 or j < 0 or i >= self.n or j >= self.n:
      raise ValueError()
    return self.adj[i][j]

  def out_edges(self, i) -> List:
    if i < 0 or i >= self.n:
      raise ValueError()
    out = []
    for j in range(0, self.n):
      if self.has_edge(i, j):
        out.append(j)
    return out

  def in_edges(self, i) -> List:
    if i < 0 or i >= self.n:
      raise ValueError()
    temp = []
    for j in range(0, self.n):
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
        for i in self.out_edges(v)[::-1]:
          if i not in array:
            stack.append(i)

    return array

  def __str__(self):
    s = ""
    for i in range(0, self.n):
      s += "%i:  %r\n" % (i, self.adj[i].__str__())
    return s
