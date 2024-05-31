class DLinkedListNode:
    # An instance of this class represents a node in Doubly-Linked List
    def __init__(self, initData, initNext, initPrevious):
        self.data = initData
        self.next = initNext
        self.previous = initPrevious

        if initNext != None:
            self.next.previous = self
        if initPrevious != None:
            self.previous.next = self

    def getData(self):
        return self.data

    def setData(self, newData):
        self.data = newData

    def getNext(self):
        return self.next

    def getPrevious(self):
        return self.previous

    def setNext(self, newNext):
        self.next = newNext

    def setPrevious(self, newPrevious):
        self.previous = newPrevious


class DLinkedList:
    # An instance of this class represents the Doubly-Linked List
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def search(self, item):
        current = self.__head
        found = False

        while current != None and not found:
            if current.getData() == item:
                found = True

            else:
                current = current.getNext()

        return found

    def index(self, item):
        current = self.__head
        found = False
        index = 0

        while current != None and not found:
            if current.getData() == item:
                found = True

            else:
                current = current.getNext()
                index = index + 1

        if not found:
            index = -1

        return index

    def add(self, item):
        # adds the item to the start of the list
        new_node = DLinkedListNode(item, None, None) 
        if self.__head != None:
            self.__head.setPrevious(new_node)
        new_node.setNext(self.__head)
        self.__head = new_node
        self.__size += 1


    def remove(self, item):
        # removes the first element in the list that is equal to the item
        current = self.__head
        previous = None
        while current.getData() != item and current.getNext() != None:
            previous = current
            current = current.getNext()
            
        if previous == None:
            self.head = None
        elif current.getNext() == None and current.getData() != item:
            return
            #doesn't change when nothing present
        elif current.getNext() == None and current.getData() == item:
            previous.setNext(None)
        else:
            previous.setNext(current.getNext())
            current.getNext().setPrevious(previous)
        self.__size += -1

    def append(self, item):
        # adds a new node to the tail of the list with item as its data
        new_node = DLinkedListNode(item, None, None) 
        current = self.__head
        
        if current == None:
            self.__head = new_node
            self.__size += 1
            return
        while current.getNext() != None:
            current = current.getNext()
        current.setNext(new_node)
        new_node.setPrevious(current)
        self.__size += 1

    def insert(self, pos, item):
        # adds a new node at the given position with item as its data.
        try:
            assert type(pos) == int
            assert pos >= 0
            
            new_node = DLinkedListNode(item,None,None)
            current = self.__head
            previous = None
            
            if pos == 0:
                self.add(item)
            elif pos == self.getSize():
                self.append(item)
            else: 
                while self.index(current.getNext().getData()) != pos and current.getNext() != None:
                    current = current.getNext() #traverse the list until the position
                    
                new_node.setNext(current.getNext())
                new_node.setPrevious(current)
                current.getNext().setPrevious(new_node)
                current.setNext(new_node)        
                self.__size += 1
            
        except AssertionError:
            print("Invalid position")
        except Exception as err:
            print(err.args)

    def pop1(self):
        # removes and returns the last item in the list
        current = self.__head
        previous = None
        while current.getNext() != None:
            previous = current
            current = current.getNext()
        if previous == None:
            self.head = None
        else:
            previous.setNext(None)
        
        self.__size += -1
        return current.getData()

    def pop(self, pos=None):
        #  removes and returns the item in the given position.
        if pos == None or self.getSize()-1 == pos:
            return self.pop1()
        
        if self.__size == 0:
            raise Exception("list empty")
        if pos >= self.getSize():
            raise Exception("position oob")
        if pos < 0:
            raise Exception("position negative")
        if type(pos) != int:
            raise Exception("position not an int")
        
        #TODO REMOVE AT NOT END

    def searchLarger(self, item):
        current = self.__head
        index = 0
        while current.getData() <= item and current.getNext() != None:
            current = current.getNext()
            index += 1
        if current.getData() > item:
            return index
        else: 
            return -1

    def getSize(self):
        return self.__size

    def getItem(self, pos):
        # returns the item at the given position.
        if self.__size == 0:
            raise Exception("list empty")
        if abs(pos) >= self.getSize():
            raise Exception("position oob")
        if type(pos) != int:
            raise Exception("position not an int")
        if pos < 0:
            pos = self.getSize() + pos
        current_index = 0
        current_node = self.__head
        while current_index != pos:
            current_node = current_node.getNext()
            current_index += 1
        return current_node.getData()

    def __str__(self):
        # create the string representation of the linked list
        current = self.__head
        string = []
        while current != None:
            string.append(str(current.getData()))
            current = current.getNext()
        return " ".join(string)


def test():

    linked_list = DLinkedList()

    is_pass = (linked_list.getSize() == 0)
    assert is_pass == True, "fail the test"

    linked_list.add("World")
    linked_list.add("Hello")

    is_pass = (str(linked_list) == "Hello World")
    assert is_pass == True, "fail the test"

    is_pass = (linked_list.getSize() == 2)
    assert is_pass == True, "fail the test"

    is_pass = (linked_list.getItem(0) == "Hello")
    assert is_pass == True, "fail the test"

    is_pass = (linked_list.getItem(1) == "World")
    assert is_pass == True, "fail the test"

    is_pass = (linked_list.getItem(0) ==
               "Hello" and linked_list.getSize() == 2)
    assert is_pass == True, "fail the test"
    
    x = linked_list.pop(1)
    is_pass = (x == "World")
    assert is_pass == True, "fail the test"
    
    is_pass = (linked_list.pop() == "Hello")
    assert is_pass == True, "fail the test"

    is_pass = (linked_list.getSize() == 0)
    assert is_pass == True, "fail the test"

    int_list2 = DLinkedList()

    for i in range(0, 10):
        int_list2.add(i)
    int_list2.remove(1)
    int_list2.remove(3)
    int_list2.remove(2)
    int_list2.remove(0)
    is_pass = (str(int_list2) == "9 8 7 6 5 4")
    assert is_pass == True, "fail the test"

    for i in range(11, 13):
        int_list2.append(i)
    is_pass = (str(int_list2) == "9 8 7 6 5 4 11 12")
    assert is_pass == True, "fail the test"

    for i in range(21, 23):
        int_list2.insert(0, i)
    is_pass = (str(int_list2) == "22 21 9 8 7 6 5 4 11 12")
    assert is_pass == True, "fail the test"
    
    x = int_list2.getSize()
    is_pass = (int_list2.getSize() == 10)
    assert is_pass == True, "fail the test"

    int_list = DLinkedList()

    is_pass = (int_list.getSize() == 0)
    assert is_pass == True, "fail the test"

    for i in range(0, 1000):
        int_list.append(i)
    correctOrder = True

    is_pass = (int_list.getSize() == 1000)
    assert is_pass == True, "fail the test"

    for i in range(0, 200):
        if int_list.pop() != 999 - i:
            correctOrder = False

    is_pass = correctOrder
    assert is_pass == True, "fail the test"

    is_pass = (int_list.searchLarger(200) == 201)
    assert is_pass == True, "fail the test"

    int_list.insert(7, 801)
    x = int_list.searchLarger(800)
    is_pass = (int_list.searchLarger(800) == 7)
    assert is_pass == True, "fail the test"
    
    x = int_list.getItem(-1)
    is_pass = (int_list.getItem(-1) == 799)
    assert is_pass == True, "fail the test"

    is_pass = (int_list.getItem(-4) == 796)
    assert is_pass == True, "fail the test"

    if is_pass == True:
        print("=========== Congratulations! Your have finished exercise 2! ============")


if __name__ == '__main__':
    test()
