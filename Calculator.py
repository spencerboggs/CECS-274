import numpy as np
import ArrayStack
import BinaryTree
import ChainedHashTable
import DLList
import operator 
import re



class Calculator:

  def __init__(self):
    self.dict = ChainedHashTable.ChainedHashTable(DLList.DLList)
    pass

  def set_variable(self, k: str, v: float):
    self.dict.add(k, v)

  def matched_expression(self, s: str) -> bool:
    stack = ArrayStack.ArrayStack()
    for c in s:
      if c == '(':
        stack.push(c)
      elif c == ')':
        if stack.size() == 0:
          return False
        stack.pop()
    return stack.size() == 0

  def print_expression(self, exp: str):
    variables = [x for x in re.split('\W+', exp) if x.isalnum()]
    for i in variables:
      if self.dict.find(i) != None:
        exp = exp.replace(i, str(self.dict.find(i)))
    print(exp)

  def _build_parse_tree(self, exp: str) -> str:
    if not self.matched_expression(exp):
      raise Exception("Unmatched expression")
    
    t = BinaryTree.BinaryTree()
    current = t.r = t.Node()

    for token in exp:
      if token == '(':
        current = current.insert_left(t.Node(token))

      if token in '+-*/':
        current.set_val(token)
        current.set_key(token)
        current = current.insert_right(t.Node())

      if token.isalpha():
        current.set_key(token)
        current.set_val(self.dict.find(token))
        current = current.parent

      if token == ')':
        current = current.parent

    return t

  def _evaluate(self, root):
    op = {
      '+': operator.add,
      '-': operator.sub,
      '*': operator.mul,
      '/': operator.truediv
    }

    if root.left != None and root.right != None:
      op = operator.getitem(op, root.v)
      left = self._evaluate(root.left)
      right = self._evaluate(root.right)
      if type(left) == str:
        # left = float(left)
        left = self.dict.find(left)
      if type(right) == str:
        # right = float(right)
        right = self.dict.find(right)
      return op(left, right)
    elif root.left == None and root.right == None:
      if root.k == None:
        raise ValueError("Missing an operand")
      if root.k != None:
        return root.k
      else:
        raise ValueError(f"Missing definition for variable {root.k}")
    else:
      raise ValueError("Missing an operand")

  def evaluate(self, exp):
    parseTree = self._build_parse_tree(exp)
    return self._evaluate(parseTree.r)
import numpy as np
import ArrayStack
import BinaryTree
import ChainedHashTable
import DLList
import operator 
import re
 
 
 
class Calculator:
 
  def __init__(self):
    self.dict = ChainedHashTable.ChainedHashTable(DLList.DLList)
    pass
 
  def set_variable(self, k: str, v: float):
    self.dict.add(k, v)
 
  def matched_expression(self, s: str) -> bool:
    stack = ArrayStack.ArrayStack()
    for c in s:
      if c == '(':
        stack.push(c)
      elif c == ')':
        if stack.size() == 0:
          return False
        stack.pop()
    return stack.size() == 0
 
  def print_expression(self, exp: str):
    variables = [x for x in re.split('\W+', exp) if x.isalnum()]
    for i in variables:
      if self.dict.find(i) != None:
        exp = exp.replace(i, str(self.dict.find(i)))
    print(exp)
 
  def _build_parse_tree(self, exp: str) -> str:
    if not self.matched_expression(exp):
      raise ValueError("Unmatched expression")
    
    characters = re.findall('[-+*/()]|\w+|\W+', exp)
    t = BinaryTree.BinaryTree()
    t.r = BinaryTree.BinaryTree.Node()
    current = t.r

    for token in characters:
      if token == '(':
        node = BinaryTree.BinaryTree.Node()
        current.insert_left(node)
        current = current.left

      elif token in '+-*/':
        current.set_key(token)
        current.set_val(token)
        node = BinaryTree.BinaryTree.Node()
        current = current.insert_right(node)

      elif token.isalnum():
        current.set_key(token)
        current.set_val(self.dict.find(token))
        current = current.parent

      elif token == ')':
        current = current.parent

      else:
        raise ValueError
      
    return t
 
    """ for token in exp:
      if token == '(':
        current = current.insert_left(t.Node(token))
 
      if token in '+-*/':
        current.set_val(token)
        current.set_key(token)
        current = current.insert_right(t.Node())
 
      if token.isalpha():
        current.set_key(token)
        current.set_val(self.dict.find(token))
        current = current.parent
 
      if token == ')':
        current = current.parent
 
    return t """
 
  def _evaluate(self, root):
    op = {
      '+': operator.add,
      '-': operator.sub,
      '*': operator.mul,
      '/': operator.truediv
    }
 
    if root.left != None and root.right != None:
      oper = op[root.k]
      return oper(self._evaluate(root.left), self._evaluate(root.right))
    elif root.left == None and root.right == None:
      if root.v != None:
        return float(root.v)
      else:
        raise ValueError(f"Missing definition for variable {root.v}")
    elif root.right != None:
      return self._evaluate(root.right)
    else:
      return self._evaluate(root.left)

    """ if root.left != None and root.right != None:
      op = operator.getitem(op, root.v)
      left = self._evaluate(root.left)
      right = self._evaluate(root.right)
      if type(left) == str:
        # left = float(left)
        left = self.dict.find(left)
      if type(right) == str:
        # right = float(right)
        right = self.dict.find(right)
      return op(left, right)
    elif root.left == None and root.right == None:
      if root.k == None:
        raise ValueError("Missing an operand")
      if root.k != None:
        return root.k
      else:
        raise ValueError(f"Missing definition for variable {root.k}")
    else:
      raise ValueError("Missing an operand") """
 
  def evaluate(self, exp):
    parseTree = self._build_parse_tree(exp)
    return self._evaluate(parseTree.r)

