from Deque_Generator import get_deque

class Stack:

  def __init__(self):
    # TODO replace pass with your implementation.
    self.__dq = get_deque()                       # initalizes a deque object

  def __str__(self):
    # TODO replace pass with your implementation.
    return str(self.__dq)                         # call to str method in deque class

  def __len__(self):
    # TODO replace pass with your implementation.
    return len(self.__dq)                         # call to len method in deque

  def push(self, val):
    self.__dq.push_back(val)                      # call to push back method in deque

  def pop(self):
    return self.__dq.pop_back()                   # call to pop back method in deque

  def peek(self):
    return self.__dq.peek_back()                  # call to peek back method in deque

# Unit tests make the main section unneccessary.
#if __name__ == '__main__':
# pass
  

