import Book
import ArrayList
import ArrayQueue
import RandomQueue
import MaxQueue
import DLList
import ChainedHashTable
import SLLQueue
import BinarySearchTree
import BinaryHeap
# import AdjacencyList
import time
 
 
class BookStore:
  '''
    BookStore: It simulates a book system such as Amazon. It allows  searching,
    removing and adding in a shopping cart. 
    '''
 
  def __init__(self):
    self.bookCatalog = None
    # self.shoppingCart = ArrayQueue.ArrayQueue()
    # self.shoppingCart = MaxQueue.MaxQueue()
    self.shoppingCart = SLLQueue.SLLQueue()
    #self.bookIndices = ChainedHashTable.ChainedHashTable()
    self.sortedTitleIndicies = BinarySearchTree.BinarySearchTree()
 
  def loadCatalog(self, fileName: str):
    '''
            loadCatalog: Read the file filenName and creates the array list with all books.
                book records are separated by  ^. The order is key, 
                title, group, rank (number of copies sold) and similar books
        '''
    self.bookCatalog = ArrayList.ArrayList()
    # self.bookCatalog = DLList.DLList()
    with open(fileName, encoding="utf8") as f:
      # The following line is the time that the computation starts
      start_time = time.time()
      for line in f:
        (key, title, group, rank, similar) = line.split("^")
        s = Book.Book(key, title, group, rank, similar)
        self.bookCatalog.append(s)
        # self.bookIndices.add(key, self.bookCatalog.size() - 1)
        self.sortedTitleIndicies.add(title, self.bookCatalog.size() - 1)
      # The following line is used to calculate the total time
      # of execution
      elapsed_time = time.time() - start_time
      print(
        f"Loading {self.bookCatalog.size()} books in {elapsed_time} seconds")
 
  def setRandomShoppingCart(self):
    q = self.shoppingCart
    start_time = time.time()
    self.shoppingCart = RandomQueue.RandomQueue()
    while q.size() > 0:
      self.shoppingCart.add(q.remove())
    elapsed_time = time.time() - start_time
    print(f"Setting randomShoppingCart in {elapsed_time} seconds")
 
  def setShoppingCart(self):
    q = self.shoppingCart
    start_time = time.time()
    # self.shoppingCart = ArrayQueue.ArrayQueue()
    while q.size() > 0:
      self.shoppingCart.add(q.remove())
    elapsed_time = time.time() - start_time
    print(f"Setting randomShoppingCart in {elapsed_time} seconds")
 
  def get_cart_best_seller(self):
    start_time = time.time()
    best_seller = self.shoppingCart.max()
    elapsed_time = time.time() - start_time
    print(
      f"getCartBestSeller returned\n{best_seller.title}\nCompleted in {elapsed_time} seconds"
    )
 
  def removeFromCatalog(self, i: int):
    '''
        removeFromCatalog: Remove from the bookCatalog the book with the index i
        input: 
            i: positive integer    
        '''
    # The following line is the time that the computation starts
    start_time = time.time()
    self.bookCatalog.remove(i)
    # The following line is used to calculate the total time
    # of execution
    elapsed_time = time.time() - start_time
    print(f"Remove book {i} from books in {elapsed_time} seconds")
 
  def addBookByIndex(self, i: int):
    '''
        addBookByIndex: Inserts into the playlist the song of the list at index i 
        input: 
            i: positive integer    
        '''
    # Validating the index. Otherwise it  crashes
    if i >= 0 and i < self.bookCatalog.size():
      start_time = time.time()
      s = self.bookCatalog.get(i)
      added = self.shoppingCart.add(s)
      elapsed_time = time.time() - start_time
      if type(added) == bool and added:
        print(f"Added to shopping cart {s} \n{elapsed_time} seconds")
      else:
        print(
          f"Attempted to add {s} to shopping cart.\nAddition was not confirmed."
        )
 
  def addBookByKey(self, key):
    start_time = time.time()
    index = self.bookIndices.find(key)
    if index is not None:
      s = self.bookCatalog.get(index)
      added = self.shoppingCart.add(s)
      elapsed_time = time.time() - start_time
      print(f"addBookByKey Completed in {elapsed_time} seconds")
 
  def addBookByPrefix(self, prefix):
    if prefix != "":
      node = self.sortedTitleIndicies.get_node(prefix)
      if node.k[0:len(prefix)] == prefix:
        s = self.bookCatalog.get(node.v)
        self.shoppingCart.add(s)
        return s.title
    return None
    
    """ start_time = time.time()
    node = self.sortedTitleIndicies.get_node(prefix).v
    title = self.bookCatalog.get(node)
    if title.title[0:len(prefix)] == prefix and prefix != '':
      self.shoppingCart.add(title)
      print(f"Added first matched title: {title.title}")
    else:
      print("Error: Prefix was not found.") """

  def bestsellers_with(self, infix, structure, n=0):
    best_sellers = None
    if structure == 1:  
      best_sellers = BinarySearchTree.BinarySearchTree()
    elif structure == 2:
      best_sellers = BinaryHeap.BinaryHeap()
    else:
      print("Invalid data structure.")

    if best_sellers is not None:
      if infix == '':
        print("Invalid infix.")
      else:
        start_time = time.time()

        if structure == 1:
          for book in self.bookCatalog:
            if infix in book.title:
              best_sellers.add(book.rank, book)
            if n != 0 and n <= best_sellers.n:
              break
          ordered = best_sellers.in_order()
          ordered_books = []
          for i in range(len(ordered)):
            ordered_books.append(ordered[-i - 1])
          for i in range(len(ordered_books)):
            print(ordered_books[i].v)



        elif structure == 2:
          for book in self.bookCatalog:
            if infix in book.title:
              book.rank *= -1
              best_sellers.add(book)
              book.rank *= -1
            if n != 0 and n <= best_sellers.n:
              break
          ordered_books = []
          for i in range(min(n, best_sellers.size())):
            ordered_books.append(best_sellers.remove())
          for i in range(len(ordered_books)):
            print(ordered_books[-i - 1])

            
        elapsed_time = time.time() - start_time
        print(f"Displayed bestsellers_with({infix}, {structure}, {n}) in {elapsed_time} seconds")
 
  def searchBookByInfix(self, infix: str, cnt: int):
    '''
        searchBookByInfix: Search all the books that contains infix
        input: 
            infix: A string    
        '''
    start_time = time.time()
    count = 0
    for i in range(self.bookCatalog.size()):
      if count == cnt:
        break
      if infix in self.bookCatalog.get(i).title:
        print(self.bookCatalog.get(i))
        count += 1
 
    elapsed_time = time.time() - start_time
    print(f"searchBookByInfix Completed in {elapsed_time} seconds")
 
  def removeFromShoppingCart(self):
    '''
        removeFromShoppingCart: remove one book from the shoppung cart  
        '''
    start_time = time.time()
    if self.shoppingCart.size() > 0:
      u = self.shoppingCart.remove()
      elapsed_time = time.time() - start_time
      print(f"removeFromShoppingCart {u} Completed in {elapsed_time} seconds")