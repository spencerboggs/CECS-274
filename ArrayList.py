import numpy as np
from Interfaces import List

class ArrayList(List):
  """ArrayList: Implementation of a List interface using Arrays. """

  def __init__(self):
    """Initialize the state (array, n and j) """

    self.n = 0
    self.j = 0
    self.a = self.new_array(1)

  def new_array(self, n: int) -> np.array:
    """
    creates a new array of size n
        Input:
            n: the size of the new array
        Return:
            An array of size n
    """
    return np.zeros(n, object)

  def resize(self):
    """creates a new array and copy the old values. """
    b = self.new_array(max(1, 2 * self.n))
    for i in range(0, self.n):
      b[i] = self.a[(i + self.j) % len(self.a)]
    self.a = b
    self.j = 0

  def get(self, i: int) -> object:
    """
    returns the element at position i
        Inputs:
            i: Index that is integer non negative and at most n
    """
    if i < 0 or i >= self.n:
      raise IndexError()

    return self.a[(i + self.j) % len(self.a)]

  def set(self, i: int, x: object) -> object:
    """
    sets the value x at the index i.
        Inputs:
            i: Index that is integer non negative and at most n
            x: Object type, i.e., any object
    """ 
    if i < 0 or i >= self.n:
      raise IndexError()
    self.a[(i + self.j) % len(self.a)] = x

  def append(self, x: object):
    """
    adds value x to the tail of the list
    """
    self.add(self.n, x)

  def add(self, i: int, x: object):
    """
    inserts value x at position i of the list and increment the number of elements 
    in the list.
      Inputs:
          i: Index that is integer non negative and at most n
          x: Object type, i.e., any object
    """
    if i < 0 or i > self.n:
      raise IndexError()
    if self.n == len(self.a):
      self.resize()
    if i < self.n / 2:
      for k in range(0, i):
        self.a[(self.j + k - 1) % len(self.a)] = self.a[(self.j + k) % len(self.a)]
      self.j = (self.j - 1) % len(self.a)
    else:
      for k in range(self.n, i, -1):
        self.a[(self.j + k) % len(self.a)] = self.a[(self.j + k - 1) % len(self.a)]
    self.a[(self.j + i) % len(self.a)] = x
    self.n += 1

  def remove(self, i: int) -> object:
    """
    removes the value at index i and returns it, if it exists.
      Inputs:
        i: index that is integer non negative at most n - 1
    """
    if i < 0 or i >= self.n:
      raise IndexError()
    x = self.a[(self.j + i) % len(self.a)]
    if i < self.n / 2:
      for k in range(i, 0, -1):
        self.a[(self.j + k) % len(self.a)] = self.a[(self.j + k - 1) % len(self.a)]
      self.j = (self.j + 1) % len(self.a)
    else:
      for k in range(i, self.n - 1):
        self.a[(self.j + k) % len(self.a)] = self.a[(self.j + k + 1) % len(self.a)]
    self.n -= 1
    if len(self.a) >= 3 * self.n:
      self.resize()
    return x

  def size(self) -> int:
    """
    returns the number of elements in this list
    """
    return self.n

  def __str__(self):
    s = "["
    for i in range(0, self.n):
      s += "%r" % self.a[(i + self.j) % len(self.a)]
      if i < self.n - 1:
        s += ","
    return s + "]"

  def __iter__(self):
    self.iterator = 0
    return self

  def __next__(self):
    if self.iterator < self.n:
      x = self.a[(self.iterator + self.j) % len(self.a)]
      self.iterator += 1
    else:
      raise StopIteration()
    return x