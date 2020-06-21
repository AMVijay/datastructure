"""
-author : Vijay/am.vijay@gmail.com/Vijayraaghavan Manoharan
"""

# Stack - LIFO data structure type implementation 
class Stack:
    __data = []

    # Adds element to Stack
    def push(self,element):
        self.__data.append(element)

    # Fetch and Deletes element from stack.
    def pop(self):
        return self.__data.pop()

# Test
stack = Stack()
stack.push("10")
stack.push(5)
stack.push("hello")

print(stack.pop())
print(stack.pop())
print(stack.pop())

