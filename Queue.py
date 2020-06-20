from Deque_Generator import get_deque

class Queue:

  def __init__(self):
    # TODO replace pass with your implementation.
    self.__dq = get_deque()                       #initalize deque object

  def __str__(self):
    # TODO replace pass with your implementation.
    return str(self.__dq)                       # call to string representation in the deque class

  def __len__(self):
    # TODO replace pass with your implementation.
    return len(self.__dq)                         # call to len in the deque class

  def enqueue(self, val):
    # TODO replace pass with your implementation.
    self.__dq.push_back(val)                      # call to push back method in the deque class

  def dequeue(self):
    # TODO replace pass with your implementation.
    return self.__dq.pop_front()                  # call to pop front method in the deque class

  def peek(self):
    # TODO replace pass with your implementation.
    return self.__dq.peek_front()                 # call to peek front method in the deque class

# Unit tests make the main section unneccessary.
#if __name__ == '__main__':
#  pass
  
