from Deque import Deque
from Linked_List import Linked_List

class Linked_List_Deque(Deque):

  def __init__(self):
    self.__list = Linked_List()

  def __str__(self):
    return str(self.__list)

  def __len__(self):
    return len(self.__list)
  
  # DO NOT CHANGE ANYTHING ABOVE THIS LINE
  
  def push_front(self, val):
    if len(self.__list) >0:                   # if length of deque > 0
      self.__list.insert_element_at(val,0)    # use insert element from linked list class to insert value at pos 0
    else:                                     # if lenth of deque =0 
      self.__list.append_element(val)         # use append element from linked list class to add first element to deque
  
  def pop_front(self):                        
    if len(self.__list)>0:                    # if length of deque > 0
      return self.__list.remove_element_at(0) # use remove element from linked list class to remove element at pos 0 and return
    else:                                     # if length of deque is 0
      return None                             # return none

  def peek_front(self):
    if len(self.__list)>0:                    # if length of deque > 0
      return self.__list.get_element_at(0)    # use get element at from linked list class to see what element is at pos 0 and return
    else:                                     # if length of deque = 0
      return None                             # return none

  def push_back(self, val):
    self.__list.append_element(val)           # use append from linked list class to add element to back of stack
  
  def pop_back(self):
    if len(self.__list)>0:                                      # if lenght of deque > 0
      return self.__list.remove_element_at(len(self.__list)-1)  # use remove element from linked list class to remove element at last position in deque and return
    else:                                                       # if length of deque = 0
      return None                                               # return none

  def peek_back(self):                                          
    if len(self.__list)>0:                                      # if length of deque > 0
      return self.__list.get_element_at(len(self.__list)-1)     # use get element at from linked list class to see last element in deque and return
    else:                                                       # if length of deque = 0
      return None                                               # return none

# Unit tests make the main section unneccessary.
if __name__ == '__main__':
  pass
