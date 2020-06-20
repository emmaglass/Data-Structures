class Binary_Search_Tree:
  # TODO.I have provided the public method skeletons. You will need
  # to add private methods to support the recursive algorithms
  # discussed in class

  class __BST_Node:
    # TODO The Node class is private. You may add any attributes and
    # methods you need. Recall that attributes in an inner class 
    # must be public to be reachabl from the the methods.

    def __init__(self, value):
      self.value = value #initialize value
      self.left = None   #initalize left
      self.right = None   #initialize right
      self.height = 1     #initialize height
      # TODO complete Node initialization

  def __init__(self):
    self.__root = None    #initialize root

    # TODO complete initialization

    # Insert the value specified into the tree at the correct
    # location based on "less is left; greater is right" binary
    # search tree ordering. If the value is already contained in
    # the tree, raise a ValueError. Your solution must be recursive.
    # This will involve the introduction of additional private
    # methods to support the recursion control variable.
    # TODO replace pass with your implementation

  def insert_element(self, value):
    current = self.__root                             #if root node is non-existent, create new node that becomes the root node
    if self.__root == None:
      self.__root = self.__BST_Node(value)
      return self.__root
    else:                                             #otherwise, if there is already a root node, call the recursive function
      self.__insert_element_helper__(value, current)

  def __insert_element_helper__(self, value, current):
    
    if current == None:                                                         #base case, insert node at correct position
      current = self.__BST_Node(value)
      return current
    if value > current.value:                                                   #if value to insert is greate than the value of the node at the current position
      current.right = self.__insert_element_helper__(value, current.right)      #call its self and change current to the right node (move right)
    elif value < current.value:                                                 #if value to insert is less than the value of the node at the current position  
      current.left = self.__insert_element_helper__(value, current.left)        #call its self and change current to the left node (move left)
    elif value == current.value:                                                #if you reach a value in the tree that is same as value you want to insert, raise value error
      raise ValueError

    if current != None:
      current.height = self.__largest_height__(current)                         #update the current height of the tree
    return current

        

    
    # Remove the value specified from the tree, raising a ValueError
    # if the value isn't found. When a replacement value is necessary,
    # select the minimum value to the from the right as this element's
    # replacement. Take note of when to move a node reference and when
    # to replace the value in a node instead. It is not necessary to
    # return the value (though it would reasonable to do so in some 
    # implementations). Your solution must be recursive. 
    # This will involve the introduction of additional private
    # methods to support the recursion control variable.
    # TODO replace pass with your implementation  

  def remove_element(self, value):
    try:                                                                        #try to remove a value by starting at the root, and call the recursive helper function
      self.__remove_element_helper__(value, self.__root)
    except ValueError:                                                          #raise a value error if the value does not exist in the tree
      raise

  def __remove_element_helper__(self, value, current):
    if current ==  None:
      raise ValueError                                                                #value to remove is not found
    
    if current.value == value:                                                        # this is the base case, the value was found at a node
      if current.left != None and current.right != None:                              # If the located value has two children, replace with minimum value from right-hand side
        curnode = current.right
        while curnode.left != None:
          curnode = curnode.left
        current.value = curnode.value                                                 # Here we equate the values, not the actual node objects
        current.right = self.__remove_element_helper__(curnode.value, current.right)
      # No children/one right child case: replace with right child (replaces with
      #    None if no children)
      elif current.left != None:                                                      # If there are either no children: replace with none, or if there is one right child: replace the node with the correct value with the right child  
        current = current.right
      else:                                                                           # If there is one left child, replace it with the left child.
        current = current.left                                                        # here we equate the node objects , not values in the node objects
    elif current.value > value:
        current.left = self.__remove_element_helper__(value, current.left)
    else:
      current.right = self.__remove_element_helper__(value, current.right)


    if current != None:
      current.height = self.__largest_height__(current)                               # Then we update the largest height of the node
      
    return current


  #  print order
    # Construct and return a string representing the in-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed as [ 4 ]. Trees with more
    # than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
    # TODO replace pass with your implementation

  def in_order(self):
    current = self.__root                                   #current node is initally the root node
    if self.__root == None:                                 # if there is nothing at the root node return empty brackets
      return ('[ ]')
    elif current.left == None and current.right == None:    # if there is only the root node in the tree, return the root node inside of brackets
      return ('[ ' + str(self.__root.value) + ' ]')
    else:
      string = self.__in_order_helper__(current)            # otherwise call the recursive function
      string = string[0:len(string)-2]                      # slice the returned string from the recursive function to exclude the last comma
      return ('[ ' + string + ' ]')                         # return the correct string representation

  def __in_order_helper__(self, current):
    string = ''                                           
    if current == None:                                     #base case, once you get to the end of a tree pathway return the string
      return string
    else:                                                   #but unitl you get to the base case, 
      string += self.__in_order_helper__(current.left)      #call the recursive function all the way to the left of the tree
      string += (str(current.value) + ", ")                 #add to the string the current value and a comma
      string += self.__in_order_helper__(current.right)     #then call the recursive function to the right of the bst
      return string


   # Construct and return a string representing the pre-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value 
    #should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
    # TODO replace pass with your implementation

  def pre_order(self):
    current = self.__root                                   # current node is initally the root node
    if self.__root == None:                                 # if there is nothing at the root node return empty brackets
      return ('[ ]')
    elif current.left == None and current.right == None:    # if there is only the root node in the tree, return the root node inside of brackets
      return ('[ ' + str(self.__root.value) + ' ]')         
    else:                                                   # otherwise call the recursive function
      string = self.__pre_order_helper__(current)       
      string = string[0:len(string)-2]                      # slice the returned string from the recursive function to exclude the last comma
      return ('[ ' + string + ' ]')                         # return the correct string representation

  def __pre_order_helper__(self, current):
    string = ''
    if current == None:                                      #base case, once you get to the end of a tree pathway return the string
      return string
    else:                                                    #but unitl you reach the base case,
      string += str(current.value) + ", "                    #add to the string the current value and the comma
      string += self.__pre_order_helper__(current.left)      #call the recursive function to the left of the bst
      string += self.__pre_order_helper__(current.right)     #call the recursive function to the right of the bst
      return string

    # Construct an return a string representing the post-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
    # TODO replace pass with your implementation

  def post_order(self):                                       # current node is initally the root node
    current = self.__root
    if self.__root == None:                                   # if there is nothing at the root node return empty brackets
      return('[ ]')                                           
    elif current.left == None and current.right == None:      # if there is only the root node in the tree, return the root node inside of brackets
      return('[ ' + str(self.__root.value) + ' ]')
    else:                                                     # otherwise call the recursive function
      string = self.__post_order_helper__(current)            
      string = string[0:len(string)-2]                        # slice the returned string from the recursive function to exclude the last comma
      return('[ ' + string + ' ]')                            # return the correct string representation

  def __post_order_helper__(self, current):
    string = ''
    if current == None:                                       # base case, once you get to the end of a tree pathway return the string                   
      return string
    else:                                                     #but until you reach the base case
      string += self.__post_order_helper__(current.left)      #call the recursive function to the left of the bst    
      string += self.__post_order_helper__(current.right)     #call the recursive function to the right of the bst
      string += str(current.value) + ", "                     #add to the string the current value and the comma
      return string


# return an integer that represents the height of the tree.
    # assume that an empty tree has height 0 and a tree with one
    # node has height 1. This method must operate in constant time.
    # TODO replace pass with your implementation

  def get_height(self):
    if self.__root == None:                 # if the tree is empty, the height of the bst is zero
      return 0
    else:
      return self.__root.height             # otherwise, return the updated height attribute

   # This function finds the height of a node in a tree
  def __largest_height__(self, current):    # this function is called in the insert and remove functions
    if current.left == None:                # if the left child of the current parent is empty, height is zero
      left_height = 0
    else:
      left_height = current.left.height     # otherwise the left height is height of the child
    if current.right == None:               # if the right child of the current parent is empty, height is zero
      right_height = 0
    else:
      right_height = current.right.height   #otherwise the right height is the height of the child
    if left_height > right_height:          # if the left height is greater than the right height
      return left_height + 1                # the new left height increases by one
    else:
      return right_height + 1               #otherwise right height increases by one


  def __str__(self):
    return self.in_order()                 #this string method returns the in order string representation of the BST

if __name__ == '__main__':
  pass

