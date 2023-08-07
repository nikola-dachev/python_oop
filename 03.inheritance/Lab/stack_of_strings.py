class BaseStack:
  def __init__(self):
    self.data = []

  def is_empty(self):
    return False if self.data else True

  def __str__(self):
    return f"[{', '.join(reversed(self.data))}]"

class AddStack(BaseStack):
  def push(self, element):
    self.data.append(element)

class PopStack(BaseStack):
  def pop(self):
    return self.data.pop()

class TopStack(BaseStack):
  def top(self):
    return self.data[-1]


class Stack(TopStack,PopStack,AddStack):
  pass