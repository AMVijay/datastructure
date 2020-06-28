"""
-author - Vijay/am.vijay@gmail.com/vijayaraaghavan manoharan
"""

# Class - List is linear datastructure List implementation
class List:
    # List Data
    __data = []

    # Add Method to insert after last node
    def add(self,element):
        self.__data.append(element)

    # Add Method to insert after specific index
    def addAtIndex(self,index,element):
        self.__data.insert(index,element)

    # Method to delete element by index
    def remove(self,index):
        return self.__data.pop(index)

    # Method to return size value
    def size(self):
        return len(self.__data)

    def fetchAllElements(self):
        return self.__data

# Test  
list = List()
list.add("10")
list.add(5)
list.addAtIndex(1,"hello")

print("Size of list :: " + str(list.size()))
print("List Values :: " + str(list.fetchAllElements()))