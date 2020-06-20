class Linked_List:
  
  class __Node:
    
    def __init__(self, val):
      # declare and initialize the private attributes
      # for objects of the Node class.
      # TODO replace pass with your implementation
      self.val = val 
      self.next = None #next arrow pointing to none
      self.prev = None #previous arrow pointing to none

  def __init__(self):
    # declare and initialize the private attributes
    # for objects of the sentineled Linked_List class
    # TODO replace pass with your implementation
    self.__header = self.__Node(None)     #header is an empty sentinel node
    self.__trailer = self.__Node(None)    #trailer is an empty sentinel node
    self.__header.next = self.__trailer   #header next arrow points to trailer
    self.__trailer.prev = self.__header   #trailer previous arrow points to header
    self.__size = 0                       #true when size of linked list is zero

  def __len__(self):
    # return the number of value-containing nodes in 
    # this list.
    # TODO replace pass with your implementation
    return self.__size

  def append_element(self, val):
    # increase the size of the list by one, and add a
    # node containing val at the new tail position. this 
    # is the only way to add items at the tail position.
    # TODO replace pass with your implementation
    new_node = Linked_List.__Node(val)      #Create a new node
    self.__trailer.prev.next = new_node     #makes next arrow of last node point at new node
    new_node.prev = self.__trailer.prev     #makes previous arrow of new node point to original last node
    self.__trailer.prev = new_node          #previous arrow or tailer points to new node
    new_node.next = self.__trailer          #next arrow of new node points to trailer
    self.__size += 1                        #increase size of linked list by 1
    

  def insert_element_at(self, val, index):
    # assuming the head position (not the header node)
    # is indexed 0, add a node containing val at the 
    # specified index. If the index is not a valid 
    # position within the list, raise an IndexError 
    # exception. This method cannot be used to add an 
    # item at the tail position.
    # TODO replace pass with your implementation
    if index >= self.__size or index < 0:       #index must be smaller than length of list and be non-negative
      raise IndexError                          #raise indexerror if index is invalid
    new_node = Linked_List.__Node(val)          #create a new node with a specific value
    if index <= self.__size//2:                 #if index is in first half of list
      cur = self.__header                       #start walk to index at head node
      for i in range(index):                    #if the node's position we are on is less than indicated index,
        cur = cur.next                          #move to the next node
      cur.next.prev = new_node                  #incorporate new node
      new_node.next = cur.next                  #incorporate new node
      new_node.prev = cur                       #incorporate new node
      cur.next = new_node                       #incorporate new node
      self.__size += 1                          #increase size of list by 1
    else:                                       #if index is in second half of list
      cur = self.__trailer                      #start walk at trailer
      for i in range(0,self.__size - index):    #walk until reach inde
        cur = cur.prev                          #advance cur with each step
      cur.prev.next = new_node                  #incorporate new node
      new_node.prev = cur.prev                  #incorporate new node
      new_node.next = cur                       #incorporate new node
      cur.prev = new_node                       #incorporate new node
      self.__size += 1                          #increase length of list by one
    

  def remove_element_at(self, index):
    # assuming the head position (not the header node)
    # is indexed 0, remove and return the value stored 
    # in the node at the specified index. If the index 
    # is invalid, raise an IndexError exception.
    # TODO replace pass with your implementation
    if index >= self.__size or index < 0:       #index mus be non-negative and less than length of list
      raise IndexError                          #if index invalid rais index error
    if index <= self.__size//2:                 #if index in fist half of list
      cur = self.__header                       #start at the header
      for i in range(index):                    #unil index
        cur = cur.next                          #advance cur one step
      cur.next.next.prev = cur                  #re-wire to remove node
      cur.next = cur.next.next                  #re-wire to remove node
      self.__size -= 1                          #decrement size by one
    else:                                       #if index in second half of list
      cur = self.__trailer                      #start walk at trailer
      for i in range(0,self.__size - index -1): #until index
        cur = cur.prev                          #advance one step backwards
      cur.prev.prev.next = cur                  #re-wire to remove node
      cur.prev = cur.prev.prev                  #re-wire to remove node
      self.__size -= 1                          #decrement size of list by one
    return cur.val                              #return value of node at index

  def get_element_at(self, index):
    # assuming the head position (not the header node)
    # is indexed 0, return the value stored in the node 
    # at the specified index, but do not unlink it from 
    # the list. If the specified index is invalid, raise 
    # an IndexError exception.
    # TODO replace pass with your implementation
    if index >= self.__size or index < 0:       #if index is negative or outside the len of list
      raise IndexError                          #raise index error
    if index <= self.__size//2:                 #if index in first half of list
      cur = self.__header                       #start at header
      for i in range(0,index+1):                #until reach index
        cur = cur.next                          #advance walk one node
    else:                                       #if index in back half of list
      cur = self.__trailer                      #start at trailer
      for i in range(0,self.__size-index):      #unitl index
        cur = cur.prev                          #advance walk backwards
    return cur.val                              #return value at the index position

  def rotate_left(self):
    # rotate the list left one position. Conceptual indices
    # should all decrease by one, except for the head, which
    # should become the tail. For example, if the list is
    # [ 5, 7, 9, -4 ], this method should alter it to
    # [ 7, 9, -4, 5 ]. This method should modify the list in
    # place and must not return a value.
    # TODO replace pass with your implementation.
    if self.__size == 0:                                  #if size of list is zero, rotating this list left is the same as doing nothing to it
      return
    elif self.__size == 1:                                #if size of list is 1, rotating this list left is the same as doing nothing to it
      return
    else:                                                 #if the size of the list is anything but 0/1 we implemnt the following algorithm to rotate the list left
      cur = self.__header                                 #start at the header node
      x = cur.next    
      self.__header.next.next.prev = self.__header        #set x equal to the node after the header node
      self.__header.next = self.__header.next.next        #sets the first node equal to the second node in the list

      self.__trailer.prev.next = x 
      x.prev = self.__trailer.prev
      x.next = self.__trailer
      self.__trailer.prev = x
  
    
  def __str__(self):
    # return a string representation of the list's
    # contents. An empty list should appear as [ ].
    # A list with one element should appear as [ 5 ].
    # A list with two elements should appear as [ 5, 7 ].
    # You may assume that the values stored inside of the
    # node objects implement the __str__() method, so you
    # call str(val_object) on them to get their string
    # representations.
    # TODO replace pass with your implementation
    if self.__size == 0:
      return '[ ]'
    elif self.__size > 0:
      list = '['
      cur = self.__header
      for i in range(0,self.__size):
        if i != self.__size-1:
          list += ' ' + str(cur.next.val) + ','
          cur = cur.next
        else:
          list += ' ' + str(cur.next.val) + ' ]'
      return list

  def __iter__(self):
    # initialize a new attribute for walking through your list
    # TODO insert your initialization code before the return
    # statement. do not modify the return statement.
    self._cur = self.__header
    return self

  def __next__(self):
    # using the attribute that you initialized in __iter__(),
    # fetch the next value and return it. If there are no more 
    # values to fetch, raise a StopIteration exception.
    # TODO replace pass with your implementation
    if self._cur.next == self.__trailer:
      raise StopIteration
    self._cur = self._cur.next
    return self._cur.val





if __name__ == '__main__':
  # Your test code should go here. Be sure to look at cases
  # when the list is empty, when it has one element, and when 
  # it has several elements. Do the indexed methods raise exceptions
  # when given invalid indices? Do they position items
  # correctly when given valid indices? Does the string
  # representation of your list conform to the specified format?
  # Does removing an element function correctly regardless of that
  # element's location? Does a for loop iterate through your list
  # from head to tail? Your writeup should explain why you chose the
  # test cases. Leave all test cases in your code when submitting.
  # TODO replace pass with your tests
  test = Linked_List()
  test.append_element(5)
  test.append_element(7)
  test.append_element(9)
  test.append_element(-4)

  # Does appending to the list add an element at the new tail 
  # position and increment the size by one?
  print("---------------------------------------------------------------------")
  print("Does appending to the list add an element at the new tail position and increment the size by one?")
  print("")
  print("The original list is " + str(test))
  print("Before appending the list, the length of the list is " + str(len(test)) + ".")
  test.append_element(10)
  print("The modified list is " + str(test))
  print("After appending the list with the value 10, the length of the list is " + str(len(test)) + ".")
  print("---------------------------------------------------------------------")

  test = Linked_List()
  #Can we append to an empty list?
  print("Does appending to an empty list add an element at the new tail position and increment the size by one?")
  print("")
  print("The original list is " + str(test))
  print("Before appending the list, the length of the list is " + str(len(test)) + ".")
  test.append_element(10)
  print("The modified list is " + str(test))
  print("After appending the list with the value 10, the length of the list is " + str(len(test)) + ".")
  print("---------------------------------------------------------------------")



  # Does inserting an item at a valid index increase the size 
  # by one and correctly modify the list's structure?
  print("Does inserting an item at a valid index increase the size by one and correctly modify the list's structure?")
  print("")
  test = Linked_List()
  test.append_element(5)
  test.append_element(7)
  test.append_element(9)
  test.append_element(-4)
  #1 Should work, inserting at a valid index
  print("The original list is " + str(test))
  print("The original list has " + str(len(test)) + " elements.")
  try:
    test.insert_element_at(21,len(test)-1)
    print("The modified list is " + str(test))
    print("The modified list has " + str(len(test)) + " elements.")
  except IndexError:
    print("Your index is invalid.")
    print("The list has not been modified.")
    print("The list is still " + str(test) + ", and the list still has " + str(len(test)) + " elements.")
  print("---------------------------------------------------------------------")

  #Does inserting an item at an invalid index leave the list completely unchanged?
  print("Does inserting an item at an invalid index leave the list completely unchanged?")
  print("")
  #1 Should not work, you cannot insert at a negative index
  print("Test 1: inserting at a invalid negaive index")
  print("The original list is " + str(test))
  print("The original list has " + str(len(test)) + " elements.")
  try:
    test.insert_element_at(21,-1)
    print("The modified list is " + str(test))
    print("The modified list has " + str(len(test)) + " elements.")
  except IndexError:
    print("Your index is invalid.")
    print("The list has not been modified.")
    print("The list is still " + str(test) + ", and the list still has " + str(len(test)) + " elements.")
  print("")
  #3 Should not work, you cannot insert at the end of a list 
  print("Test 2: inserting at the end of the list, an invalid index")
  print("The original list is " + str(test))
  print("The original list has " + str(len(test)) + " elements.")
  try:
    test.insert_element_at(21,len(test))
    print("The modified list is " + str(test))
    print("The modified list has " + str(len(test)) + " elements.")
  except IndexError:
    print("Your index is invalid.")
    print("The list has not been modified.")
    print("The list is still " + str(test) + ", and the list still has " + str(len(test)) + " elements.")
  print("")
  #3 Should not work, you cannot insert beyond the length of the list
  print("Test 3: inserting beyond the end of the list, an invalid index")
  print("The original list is " + str(test))
  print("The original list has " + str(len(test)) + " elements.")
  try:
    test.insert_element_at(21,len(test)+1)
    print("The modified list is " + str(test))
    print("The modified list has " + str(len(test)) + " elements.")
  except IndexError:
    print("Your index is invalid.")
    print("The list has not been modified.")
    print("The list is still " + str(test) + ", and the list still has " + str(len(test)) + " elements.")
  print("")
  #create new empty linked list
  test = Linked_List()
  #4 Should not work, you cannot insert a value into an empty list, the same as append
  print("Test 4: inserting in an empty list")
  print("The original list is " + str(test))
  print("The original list has " + str(len(test)) + " elements.")
  try:
    test.insert_element_at(21,len(test))
    print("The modified list is " + str(test))
    print("The modified list has " + str(len(test)) + " elements.")
  except IndexError:
    print("Your index is invalid.")
    print("The list has not been modified.")
    print("The list is still " + str(test) + ", and the list still has " + str(len(test)) + " elements.")
  print("---------------------------------------------------------------------")



  #Does removing an item at a valid index decrease the size by one and correctly
  # modify ths list's structure?
  print("Does inserting an item at a valid index decrease the size by one and correctly modify the lists structure?")
  print()
  #Create a new linked list with values
  test = Linked_List()
  test.append_element(5)
  test.append_element(7)
  test.append_element(9)
  test.append_element(-4)
  #1 Should work, removing at a valid index
  print("Test 1: removing at a valid index ")
  print("The original list is " + str(test))
  print("The original list has " + str(len(test)) + " elements.")
  try:
    test.remove_element_at(len(test)-1)
    print("The modified list is " + str(test))
    print("The modified list has " + str(len(test)) + " elements.")
  except IndexError:
    print("Your index is invalid.")
    print("The list has not been modified.")
    print("The list is still " + str(test) + ", and the list still has " + str(len(test)) + " elements.")
  print()

  #2 Should work, you should be able to remove a value from a list with only one value
  print("Test 2: removing at a valid index in a list with one value")
    #create list with one value
  test=Linked_List()
  test.append_element(5)
  print("The original list is " + str(test))
  print("The original list has " + str(len(test)) + " elements.")
  try:
    test.remove_element_at(len(test)-1)
    print("The modified list is " + str(test))
    print("The modified list has " + str(len(test)) + " elements.")
  except IndexError:
    print("Your index is invalid.")
    print("The list has not been modified.")
    print("The list is still " + str(test) + ", and the list still has " + str(len(test)) + " elements.")
  print("---------------------------------------------------------------------")


  #Does removing an item at an invalid index leave the list completely uncahnged?
  print("Does removing an item at an invalid index leave the list completely unchanged?")
  print()
  #create list with values
  test = Linked_List()
  test.append_element(5)
  test.append_element(7)
  test.append_element(9)
  test.append_element(-4)
  #1 Should not work, you cannot remove a value if the index is out of range
  print("Test 1: Removing at an invalid negative index")
  print("The original list is " + str(test))
  print("The original list has " + str(len(test)) + " elements.")
  try:
    test.remove_element_at(-2)
    print("The modified list is " + str(test))
    print("The modified list has " + str(len(test)) + " elements.")
  except IndexError:
    print("Your index is invalid.")
    print("The list has not been modified.")
    print("The list is still " + str(test) + ", and the list still has " + str(len(test)) + " elements.")
  print()

  #2 Should not work, you cannot remove a value if the index is greater than
  #  the length of the list
  print("Test 2: Removing at an invalid index at position greater than length of list")
  print("The original list is " + str(test))
  print("The original list has " + str(len(test)) + " elements.")
  try:
    test.remove_element_at(len(test)+1)
    print("The modified list is " + str(test))
    print("The modified list has " + str(len(test)) + " elements.")
  except IndexError:
    print("Your index is invalid.")
    print("The list has not been modified.")
    print("The list is still " + str(test) + ", and the list still has " + str(len(test)) + " elements.")
  print()

  #Create new empty list
  test = Linked_List()
  #3 Should not work, you cannot remove a value if the list is empty
  print("Test 3: Removing from an empty list")
  print("The original list is " + str(test))
  print("The original list has " + str(len(test)) + " elements.")
  try:
    test.remove_element_at(len(test))
    print("The modified list is " + str(test))
    print("The modified list has " + str(len(test)) + " elements.")
  except IndexError:
    print("Your index is invalid.")
    print("The list has not been modified.")
    print("The list is still " + str(test) + ", and the list still has " + str(len(test)) + " elements.")
  print()
  print("---------------------------------------------------------------------")

  #Does length always return the number of values stored in the list 
  #not including sentinel nodes
  print("Does length always return the number of values stored in the list not including sentinel nodes?")
  print()

  #1 Testing with a non-empty list
  print("Test 1: Testing len() with a non-empty list")
  #Let's make a list with values
  test = Linked_List()
  test.append_element(5)
  test.append_element(7)
  test.append_element(9)
  test.append_element(-4)
  #Let's test the iterator first, 
  print("The list is:" + str(test))
  values = 0
  print('Testing iterator:')
  for val in test:
    print(val)
    values += 1
  print("There are " + str(values) + " values in the linked list according to the iterator. ")
  # Now if we use the length function, we should also get 4 if it ignores the header and trailer nodes
  print("Using the len() function, the length of our linked list is " + str(len(test)) +".")
  print("So, we know the len function ignores the header and trailer sentinel nodes because it outputs the same length as the iterator.")
  print()

  #2 Testing with an empty list
  print("Test 2: Testing len() with an empty list")
  #Let's create an empty list
  test = Linked_List()
  #Let's test the iterator first, 
  print("The list is:" + str(test))
  values = 0
  print('Testing iterator:')
  for val in test:
    print(val)
    values += 1
  print("There are " + str(values) + " values in the linked list according to the iterator. ")
  # Now if we use the length function, we should also get 4 if it ignores the header and trailer nodes
  print("Using the len() function, the length of our linked list is " + str(len(test)) +".")
  print("So, we know the len function ignores the header and trailer sentinel nodes because it outputs the same length as the iterator.")
  print("Additionally, if it counted header and trailer sentinel nodes, the length of an empty list would be 2.")
  print()
  print("---------------------------------------------------------------------")

  #Is the string representation fo your list correct for a variety of lengths?
  print("Is the string representation of your list correct for a variety of lengths?")
  print()
  
  #create an empty list
  test = Linked_List()
  #1 Printing an empty list
  print("Test 1: Format of an empty list")
  print("The correct format of an empty list should be: [ ]")
  print("The str() format of an empty list is: " + str(test))
  print()
  
  #append list with one value
  test.append_element(5)
  #2 Printing a list with one value
  print("Test 2: Format of a list with one value")
  print("The correct formato of a list with one value should be: [ value ]")
  print("The str() format of a list with one value is: " + str(test))
  print()
  
  #append list with two more values
  test.append_element(9)
  test.append_element(3)
  #3 Printing a list with more than one value
  print("Test 3: Format of a list with more than one value")
  print("The correct format of a list with one value should be: [ value, value, value ]")
  print("The str() format of a list with more than one value is: " + str(test))
  print()
  print("---------------------------------------------------------------------")

  #Does a for loop like for val in my_list visit every value
  print("Does a for loop like 'for val in my_list' visit every value?")
  print()
  print("The list is:" + str(test))
  print("The iterator prints all values in the list:")
  for val in test:
    print(val)
  print("---------------------------------------------------------------------")

  #Does get_element_at() retrieve the value at the specified valid index?
  print("Does get_element_at() retrieve the value at the specified valid index and leave the list unchanged?")
  print()
  #1 Should work, if the index is valid, it should be able to retrieve the value
  print("Test 1: get_element_at() a valid index")
  print("The original list is:" + str(test))
  try:
    print("The value at index " + str(len(test)-1) + " is " + str(test.get_element_at(len(test)-1)))
    print("The list after get_element_at() applied is: " + str(test))
  except IndexError:
    print("Your index is invalid.")
    print("get_element_at() could not retrieve the value at your specified index.")
    print("The list is still: " + str(test))

  print("---------------------------------------------------------------------")

  #Does get_element_at() of an invalid index leave the list completely unchanged?
  print("Does get_element_at() of an invalid index leave the list completely unchanged?")
  print()
  
  #1 getelementat in empty list should fail
  print("Test 1: get_element_at() in an empty list")
   #create empty list
  test = Linked_List()
  print("The original list is:" + str(test))
  try:
    print("The value at index 0 is " + str(test.get_element_at(0)))
    print("The list after get_element_at() applied is: " + str(test))
  except IndexError:
    print("Your index is invalid.")
    print("get_element_at() could not retrieve the value at your specified index.")
    print("The list is still: " + str(test))
  print()
  
  #2  get_element_at() with a negative index, should fail
  print("Test 2: get_element_at() with an invalid negative index")
    #create a list with values
  test = Linked_List()
  test.append_element(5)
  test.append_element(7)
  test.append_element(9)
  test.append_element(-4)
  print("The original list is: " + str(test))
  try:
    print("The value at index -1 is " + str(test.get_element_at(-1)))
    print("The list after get_element_at() applied is: " + str(test))
  except IndexError:
    print("Your index is invalid.")
    print("get_element_at() could not retrieve the value at your specified index.")
    print("The list is still: " + str(test))
  print()

  #3 get_element_at() with an index > len(test), should fail
  print("Test 3: get_element_at() with an invalid index > len(test)")
  print("The original list is: " + str(test))
  try:
    print("The value at index " + str(len(test)+1) + " is " + str(test.get_element_at(len(test)+1)))
    print("The list after get_element_at() applied is: " + str(test))
  except IndexError:
    print("Your index is invalid.")
    print("get_element_at() could not retrieve the value at your specified index.")
    print("The list is still: " + str(test))
  print("---------------------------------------------------------------------")

  #Does rotate_left rotate all values left one position?
  print("Does rotate_left() rotate all values left one position?")
  print()

  #1 Rotating an empty list should have no effect on the list
  print("Test 1: Rotating an empty list")
  # create empty list
  test = Linked_List()
  #test.append_element(5)
  print("The original list is: " + str(test))
  test.rotate_left()
  print("The list after rotation is: " + str(test))
  print()

  #2 Rotating a list with one value should have no effect on the list
  print("Test 2: Rotating a list with one value")
  #append list with one value
  test.append_element(5)
  print("The original list is: " + str(test))
  test.rotate_left()
  print("The list after roation is: " + str(test))
  print()

  #3 Rotating a list with two values should switch the values
  print("Test 3: Rotating a list with two values")
  #append list with another value
  test.append_element(3)
  print("The original list is: " + str(test))
  test.rotate_left()
  print("The list after roation is: " + str(test))
  print()

  #4 Rotating a list with multiple values should switch everything to the left one
  print("Test 4: Rotating a list with multiple values")
  #append list with 2 more values
  test.append_element(7)
  test.append_element(10)
  print("The original list is: " + str(test))
  test.rotate_left()
  print("The list after roation is: " + str(test))
  print("---------------------------------------------------------------------")















  

  



  

  
  
