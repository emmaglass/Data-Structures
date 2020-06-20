from Deque import Deque

class Array_Deque(Deque):

  def __init__(self):
    # capacity starts at 1; we will grow on demand.
    self.__capacity = 1                         # initalize capacity as one
    self.__contents = [None] * self.__capacity  # initalize contents as array of none
    self.__front = 0                            # initalize front =0 
    self.__back = 0                             # initalize back =0
    self.__size = 0                             # initalize size = 0
    # TODO replace pass with any additional initializations you need.
    
  def __str__(self):
    # TODO replace pass with an implementation that returns a string of
    # exactly the same format as the __str__ method in the Linked_List_Deque.
    if self.__front > self.__back:                                                        # if position of front is to the right of the position of back in contents array
      string = str(self.__contents[self.__front:] + self.__contents[:self.__back+1])      # this is how we contatenate the string representation
      string = string.replace('[','[ ')                                                   # this makes the brackets be in the same format as linked list deque
      string = string.replace(']',' ]')
      string = string.replace("'",'')                                                     # this removes the quotes around the string 
      return string                                 
    elif self.__size == 0:                                                                # if deque is empty return empty brackets
      return '[ ]'
    else:
      string = str(self.__contents[self.__front:self.__back+1])                           # if the front is to the left of the back in the contents array
      string = string.replace('[','[ ')                                                   # this makes the brackets be in the same format as the linked list deque 
      string = string.replace(']',' ]')
      string = string.replace("'",'')                                                     # this removes the quotes around the string 
      return string
    
  def __len__(self):
    # TODO replace pass with an implementation that returns the number of
    # items in the deque. This method must run in constant time.
    return self.__size                                                        # returns the size of the deque

  def __grow(self):
    # TODO replace pass with an implementation that doubles the capacity
    # and positions existing items in the deque starting in cell 0 (why is
    # necessary?)
    self.__capacity = self.__capacity * 2                                 #doubles the capacity
    old_array = self.__contents                                           #set old array equal to contents
    self.__contents = [None] * self.__capacity                            #makes new empty double the size contents array
    walk = self.__front                                                   #walk starts at front position
    for i in range(self.__capacity):                                      #for every value in the contents array
        self.__contents[i] = old_array[walk]                              # value in contents array at index is equal to the old array at the front position
        walk = (1 + walk) % len(old_array)                                # change the walk position
    self.__front = 0                                                      # set front equal to zero in the new array
    self.__back = (self.__front + self.__size -1) % len(self.__contents)  # change back position

    
    

    
  def push_front(self, val):
    # TODO replace pass with your implementation, growing the array before
    # pushing if necessary.
    if self.__size == len(self.__contents):                 #if the size of deque is equal to the size of the contents array
      self.__grow()                                         #call to the grow function
    self.__front = (self.__front-1) % len(self.__contents)  #move the front position by one
    self.__contents[self.__front] = val                     #put the specified val in the new front position
    self.__size +=1                                         # increment size of deque by one
    
  def pop_front(self):
    # TODO replace pass with your implementation. Do not reduce the capacity.
    if self.__size > 0:                                       # if size of deque is greater than zero
      popd = self.__contents[self.__front]                    # save the value at the front of the deque in popd variable
      self.__contents[self.__front] = None                    # set the cell tht corresponds to front as empty
      self.__front = (self.__front+1) % len(self.__contents)  # change the position of front by one
      self.__size -= 1                                        # decrement the size of the deque by one
      return popd                                             # return the removed value
    else:                                                     # if size of deque is zero
      return None                                             # return none
    
  def peek_front(self):
    # TODO replace pass with your implementation.
    if self.__size > 0:                                       # if size of deque is greater than zero
      return self.__contents[self.__front]                    # return the value at the front of the deque
    else:                                                     # if the size of the deque is zero
      return None                                             # return none
    
  def push_back(self, val):
    # TODO replace pass with your implementation, growing the array before
    # pushing if necessary.
    if self.__size == len(self.__contents):                   # if the size of the deque is equal to the size of the contents array
        self.__grow()                                         #call to the grow funciton
    self.__back = (self.__back +1) % len(self.__contents)     # change the position of the back
    self.__contents[self.__back] = val                        # put the specified value in the new back position
    self.__size += 1                                          # increment size by one
    
  
  def pop_back(self):
    # TODO replace pass with your implementation. Do not reduce the capacity.
    if self.__size > 0:                                       # if size of deque is greater than zero
      popd = self.__contents[self.__back]                     #save the value at the back of the deque in the popd variable
      self.__contents[self.__back] = None                     # change the value at the back position to none
      self.__back = (self.__back-1) % len(self.__contents)    # change the position of the back index
      self.__size -= 1                                        # decrement the size of the deque by one
      return popd                                             # return the removed value
    else:                                                     # if the length of the deque is zero
      return None                                             # return none

  def peek_back(self):      
    # TODO replace pass with your implementation.
    if self.__size > 0:                                       # if the size of the deque is greate than zero
      return self.__contents[self.__back]                     #return the value at the back position of the deque
    else:                                                     # if the deque has size 0
      return None                                             # return none

# No main section is necessary. Unit tests take its place.
if __name__ == '__main__':
  pass

  
  


