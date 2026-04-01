import ctypes
 
class CustomList:
    def __init__(self):
        initial_capacity = 1
        self.capacity = initial_capacity
        self.size = 0
        self.array = self.__create_array(self.capacity)
 
    def __create_array(self, capacity):
        # Create a new array with the given capacity
        return (capacity * ctypes.py_object)()
 
    def __resize(self, new_capacity):
        new_array = self.__create_array(new_capacity)
        for i in range(self.size):
            new_array[i] = self.array[i]
        
        self.array = new_array
        self.capacity = new_capacity
 
    def append(self, item):
        if self.size == self.capacity:
            self.__resize(2 * self.capacity)
        self.array[self.size] = item
        self.size += 1
    
    def __len__(self):
        return self.size
    
    def __str__(self):
        if self.size == 0:
            return '[]'
        output = ''
        for i in range(self.size):
            output += str(self.array[i]) + ', '
        return '[' + output[:-2] + ']'
    
    def pop(self):
        if self.size == 0:
            return 'Empty List, IndexError: pop from empty list'
        
        popped_item = self.array[self.size - 1]
        self.size -= 1
        return popped_item
    
    def __getitem__(self, index):
        if 0 <= index < self.size:
            return self.array[index]
        else:
            return 'Index Error: Invalid index'
        
    def clear(self):
        self.size = 0
 
    def insert(self, position, element):
        if position < 0 or position > self.size:
            return 'Index Error: Invalid position'
        
        if self.size == self.capacity:
            self.__resize(2 * self.capacity)
        
        for index in range(self.size, position, -1):
            self.array[index] = self.array[index - 1]
        
        self.array[position] = element
        self.size += 1
 
    def remove(self, element):
        for i in range(self.size):
            if self.array[i] == element:
                for j in range(i, self.size - 1):
                    self.array[j] = self.array[j + 1]
                self.size -= 1
                return
        return 'Element not found'

        

myList = CustomList()
myList.append(11)
myList.append(22)
myList.append(33)
myList.append(44)
myList.append(55)

print(myList)
print(myList.pop())
print(myList)

print(myList[2])

#myList.clear()
print(myList)
myList.insert(2, 100)
print(myList)

myList.remove(11)
print(myList)