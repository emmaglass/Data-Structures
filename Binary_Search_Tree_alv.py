class Binary_Search_Tree:


  class __BST_Node:
    
    def __init__(self, value):
      self.value = value
      self.left = None
      self.right = None
      self.height = 1


    def __str__(self):
      return str(self.value)


  def __init__(self):
    self.__root = None

  def insert_element(self, value):
    # Insert the value specified into the tree at the correct
    # location based on "less is left; greater is right" binary
    # search tree ordering. If the value is already contained in
    # the tree, raise a ValueError. Your solution must be recursive.
    # This will involve the introduction of additional private
    # methods to support the recursion control variable.
    if self.__root == None:
        self.__root = self.__BST_Node(value)
        return self.__root
    else:
      self.__root = self.__insert_element_helper(value, self.__root)

  def __insert_element_helper(self, value, current):
    if current == None: # At the spot of insertion
      node = self.__BST_Node(value)
      return node
    else:
      if value > current.value:
        current.right = self.__insert_element_helper(value, current.right)
      elif value < current.value:
        current.left = self.__insert_element_helper(value, current.left)
      else:
        raise ValueError # Duplicate values are invalid

    current.height = self.__largest_height(current) # Sets height of node
    return self.__balance(current) # returns balanced tree

  def remove_element(self, value):
    # Remove the value specified from the tree, raising a ValueError
    # if the value isn't found. When a replacement value is necessary,
    # select the minimum value to the from the right as this element's
    # replacement. Take note of when to move a node reference and when
    # to replace the value in a node instead. It is not necessary to
    # return the value (though it would reasonable to do so in some 
    # implementations). Your solution must be recursive. 
    # This will involve the introduction of additional private
    # methods to support the recursion control variable.
    try:
      self.__root = self.__remove_element_helper(value, self.__root)
    except ValueError:
      raise # Re-raises ValueError

  def __remove_element_helper(self, value, current):
    if current == None:
      raise ValueError # value to remove is not found
    
    if current.value == value: # base case: found value at node
      # Two child case: replace with minimum value from right-hand side
      if current.left == None:
        current = current.right
      elif current.left != None and current.right != None:
        curnode = current.right
        while curnode.left != None:
          curnode = curnode.left
        current.value = curnode.value # equate values, not nodes
        current.right = self.__remove_element_helper(curnode.value, current.right)
      # No children/one right child case: replace with right child (replaces with
      #    None if no children)
      # One left child: replaces node with left child
      else:
        current = current.left # equate nodes, not values
    elif current.value > value:
      current.left = self.__remove_element_helper(value, current.left)
    else:
      current.right = self.__remove_element_helper(value, current.right)


    if current != None:
      current.height = self.__largest_height(current) # Sets height of node
      
    return self.__balance(current)  # returns balanced tree
      
  def in_order(self):
    # Construct and return a string representing the in-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed as [ 4 ]. Trees with more
    # than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
    if self.__root == None:
      return "[ ]"
    elif self.__root.left == None and self.__root.right == None:
      return ('[ ' + str(self.__root) + ' ]')
    else:
      string = self.__in_order_helper(self.__root)
      string = string[0:len(string)-2] # deletes extra comma
      return ('[ ' + string + ' ]')

  def __in_order_helper(self, current):
    string = ''
    if current == None:
      return string
    else:
      string += str(self.__in_order_helper(current.left))
      string += str(current) + ', '
      string += str(self.__in_order_helper(current.right))
      return string

  def pre_order(self):
    # Construct and return a string representing the pre-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
    if self.__root == None:
      return '[ ]'
    elif self.__root.left == None and self.__root.right == None:
      return ('[ ' + str(self.__root) + ' ]')
    else:
      string = self.__pre_order_helper(self.__root)
      string = string[0:len(string)-2]
      return ('[ ' + string + ' ]')

  def __pre_order_helper(self, current):
    string = ''
    if current == None:
      return string
    else:
      string += str(current) + ', '
      string += self.__pre_order_helper(current.left)
      string += self.__pre_order_helper(current.right)
      return string


  def post_order(self):
    # Construct an return a string representing the post-order
    # traversal of the tree. Empty trees should be printed as [ ].
    # Trees with one value should be printed in as [ 4 ]. Trees with
    # more than one value should be printed as [ 4, 7 ]. Note the spacing.
    # Your solution must be recursive. This will involve the introduction
    # of additional private methods to support the recursion control 
    # variable.
    if self.__root == None:
      return '[ ]'
    elif self.__root.left == None and self.__root.right == None:
      return ('[ ' + str(self.__root) + ' ]')
    else:
      string = self.__post_order_helper(self.__root)
      string = string[0:len(string)-2]
      return ('[ ' + string + ' ]')

  def __post_order_helper(self, current):
    string = ''
    if current is None:
      return string
    else:
      string += self.__post_order_helper(current.left)
      string += self.__post_order_helper(current.right)
      string += str(current) + ", "
      return string

  def get_height(self):
    # return an integer that represents the height of the tree.
    # assume that an empty tree has height 0 and a tree with one
    # node has height 1. This method must operate in constant time.
    if self.__root == None:
      return 0
    else:
      return self.__root.height


  # This function finds the height of a node in a tree
  def __largest_height(self, current):
    
    # Without these conditionals the program crashes when trying to find None.height
    if current.left == None:
      left_height = 0
    else:
      left_height = current.left.height


    if current.right == None:
      right_height = 0
    else:
      right_height = current.right.height
    
    if left_height > right_height:
      return left_height + 1
    else:
      return right_height + 1


    
  # return value 0 means balanced, 1 means left heavy, 2 means right heavy
  
  # Shift variable is the amount by which the tree must be imbalanced to
  #    return a value of 1 or 2. This is necessary, because trees with
  #    an imbalance of 1 are still valid, but we still need to calculate
  #    the balance of trees that are only imabalanced by one in the
  #    __balance method, in case we need to preform a double shift
  def __determine_heaviness(self, t, shift):
    left_heavy = False
    right_heavy = False


    if t == None:
      return 0
    
    if t.right != None:
      right_ch_h = t.right.height
    else:
      right_ch_h = 0

    if t.left != None:
      left_ch_h = t.left.height
    else:
      left_ch_h = 0

    if (left_ch_h - shift) >= right_ch_h:
      left_heavy = True
    elif (right_ch_h - shift) >= left_ch_h:
      right_heavy = True


    if left_heavy is False and right_heavy is False:
      return 0 # balanced case
    elif left_heavy is True:
      return 1 # left heavy
    elif right_heavy is True:
      return 2 # right heavy



  # __shift_up_left and __shift_up_right are used in __balance. These
  #    methods replace the root of a tree with its left or right child
  #    in the algorithm defined by AVL tree single rotations. For double
  #    rotations, two shift function calls are necessary.
  def __left_shift(self, t):
    t_value = t.value
    t_left = t.left
    t = t.right
    t_float = t.left

    new_l = self.__BST_Node(t_value)
    new_l.right = t_float
    new_l.left = t_left
    new_l.height = self.__largest_height(new_l)

    t.left = new_l
    t.height = self.__largest_height(t)

    return t
    
  def __right_shift(self, t):
    t_value = t.value
    t_right = t.right
    t = t.left
    t_float = t.right
      
    new_r = self.__BST_Node(t_value)
    new_r.right = t_right
    new_r.left = t_float
    new_r.height = self.__largest_height(new_r)
    
    t.right = new_r
    t.height = self.__largest_height(t)

    return t


  # This method balances a tree. It is called inside insert_element
  #    and remove_element
  def __balance(self, t):
    # Finds balance of root node
    parent_bal = self.__determine_heaviness(t, 2)


    # left heavy checking for kinks in tree
    if parent_bal == 1:
      left_ch_bal = self.__determine_heaviness(t.left, 1)

        # left heavy single rotation
    if parent_bal == 1 and left_ch_bal != 2:
      t = self.__right_shift(t)
      print('Left single rotation')

    # right heavy checking for kinks in tree
    if parent_bal == 2:
      right_ch_bal = self.__determine_heaviness(t.right, 1)


    # left heavy double rotation
    elif parent_bal == 1 and left_ch_bal == 2:
      t.left = self.__left_shift(t.left)
      t = self.__right_shift(t)

    # right heavy single rotation
    elif parent_bal == 2 and right_ch_bal != 1:
      t = self.__left_shift(t)


    # right heavy double rotation
    elif parent_bal == 2 and right_ch_bal == 1:
      t.right = self.__right_shift(t.right)
      t = self.__left_shift(t)

    return t


  def to_list(self):
    return self.__to_list_helper(self.__root)

  def __to_list_helper(self, current):
    list = [ ]
    if current is None:
      return [ ]
    else:
      list += self.__to_list_helper(current.left)
      list += [current.value]
      list += self.__to_list_helper(current.right)
      return list

  def __str__(self):
    return self.in_order()
    



if __name__ == '__main__':
  tree = Binary_Search_Tree()
  tree.insert_element(1)
  tree.insert_element(2)
  tree.insert_element(3)
  tree.insert_element(4)
  tree.insert_element(5)
  '''tree.insert_element(62)
  tree.insert_element(95)
  tree.insert_element(37)
  tree.insert_element(53)
  tree.insert_element(68)
  tree.insert_element(83)
  tree.insert_element(54)
  tree.remove_element(95)'''

  print(tree.pre_order())
  #print(tree.in_order())
  #print(tree.post_order())