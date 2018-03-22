class DoubleLinkedList:

    class _Node:
        """Lightweight, nonpublic class for storing a doubly linked node."""
        __slots__ = '_element', '_next', '_prev'         # streamline memory usage

        def __init__(self, element, prev, next):      # initialize node's fields
            self._element = element               # reference to user's element
            self._prev = prev 					  # reference to prev node
            self._next = next                     # reference to next node




    def __init__(self):
        """Create an empty linkedlist."""
        self._head = None
        self._tail = None
        self._size = 0


    def __len__(self):
        """Return the number of elements in the list."""
        return self._size

    def is_empty(self):
        """Return True if the list is empty."""
        return self._size == 0

    def first(self):
        """Return (but do not remove) the element at the front of the list.
        Raise Empty exception if the list is empty.
        """
        if self.is_empty():
            raise Empty('list is empty')
        return self._head._element              # front aligned with head of list

    def last(self):
        """Return (but do not remove) the element at the end of the list.

        Raise Empty exception if the list is empty.
        """
        if self.is_empty():
            raise Empty('list is empty')
        return self._tail._element


    def delete_first(self):
        """Remove and return the first element of the list.

        Raise Empty exception if the list is empty.
        """
        if self.is_empty():
            raise Empty('list is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():                     # special case as deque is empty
            self._tail = None                     # removed head had been the tail
        else:
            self._head._prev = None
        return answer

    def delete_last(self):
        """Remove and return the last element of the list.

        Raise Empty exception if the list is empty.
        """
        if self.is_empty():
            raise Empty('list is empty')
        answer = self._tail._element
        self._tail = self._tail._prev
        self._size -= 1
        if self.is_empty():                     # special case as deque is empty
            self._head = None                     # removed tail had been the head
        else:
            self._tail._next = None
        return answer


    def add_first(self, e):
        """Add an element to the front of list."""
        newest = self._Node(e, None, self._head)   # node will be new head node, next point to old head
        if self.is_empty():
            self._tail = newest                   # special case: previously empty
        else:
            self._head._prev = newest
        self._head = newest
        self._size += 1


    def add_last(self, e):
        """Add an element to the back of list."""
        newest = self._Node(e, self._tail, None)            # node will be new tail node, prev point to old tail
        if self.is_empty():
            self._head = newest                   # special case: previously empty
        else:
            self._tail._next = newest
        self._tail = newest                     # update reference to tail node
        self._size += 1


    def __str__(self):
        result = []
        result.append("head <--> ")
        curNode = self._head
        while (curNode is not None):
            result.append(str(curNode._element) + " <--> ")
            curNode = curNode._next
        result.append("tail")
        return "".join(result)

    def diff(self, otherlist):
        # Determines which elements of a list are not contained in another list.
        # @parameter1: otherlist, the linkedlist to be compared with self linkedlist
        # @return: A new DoubleLinkedList of elements. Those elements exist in the self list, but not otherlist.
        #		
        # Example:
        # self list: head <--> 5 <--> 3 <--> 2 <--> 1 <--> tail
        # otherlist: head <--> 1 <--> 4 <--> tail
        # >>> l.diff(otherlist)
        # should return: head <--> 5 <--> 3 <--> 2 <--> tail   (Order doesn't matter.)
		
        # To do
        ite = self._head

        result = DoubleLinkedList()
        n = self.__len__()

        while n != 0:
            flag = False
            check_node = otherlist._head
            m = otherlist.__len__()
            while m != 0:
                if check_node._element == ite._element:
                    flag = True
                    break
                check_node = check_node._next
                m -=1
            if not flag:


                result.add_first(ite._element)
            ite = ite._next
            n -= 1
        return result





    def superFeed(self, otherlist, n):
        # Removes several first elements from a list and inserts them as the first
        # elements of another list in the original order.
        # @parameter1: otherlist, remove elements from this list.
        # @parameter2: n, number of elements to remove
        # @return: Nothing
        #
        # Example:
        # self list: head <--> 5 <--> 3 <--> 2 <--> 1 <--> tail
        # otherlist: head <--> 1 <--> 4 <--> 7 <--> 9 <--> tail
        # >>> l.superFeed(otherlist, 3)
        # l should become:
        # head <--> 1 <--> 4 <--> 7 <--> 5 <--> 3 <--> 2 <--> 1 <--> tail
        # otherlist should become:
        # head <--> 9 <--> tail

        # To do
        temp = DoubleLinkedList()
        while n !=0:
            temp.add_first(otherlist.delete_first())
            n -= 1
        while not temp.is_empty():
            self.add_first(temp.delete_first())








diffTest = True
superFeedTest = True

if (diffTest):
    print("-----------Testing diff-------------")
    l1 = DoubleLinkedList()
    l2 = DoubleLinkedList()
    for i in range(10):
        l1.add_first(i * 2)
    for j in range(10):
        l2.add_first(j * 3)
    print(l1)   # 18 <--> 16 <--> 14 <--> 12 <--> 10 <--> 8 <--> 6 <--> 4 <--> 2 <--> 0 <--> None
    print(l2)   # 27 <--> 24 <--> 21 <--> 18 <--> 15 <--> 12 <--> 9 <--> 6 <--> 3 <--> 0 <--> None
    print(l1.diff(l2))  # 2 <--> 4 <--> 8 <--> 10 <--> 14 <--> 16 <--> None

if (superFeedTest):
    print("-----------Testing superFeed-------------")
    l1 = DoubleLinkedList()
    l2 = DoubleLinkedList()
    for i in range(5):
        l1.add_first(i * 2)
    for j in range(5):
        l2.add_first(j * 3)
    print(l1) # 8 <--> 6 <--> 4 <--> 2 <--> 0 <--> None
    print(l2) # 12 <--> 9 <--> 6 <--> 3 <--> 0 <--> None
    l1.superFeed(l2, 3)
    print(l1) # 12 <--> 9 <--> 6 <--> 8 <--> 6 <--> 4 <--> 2 <--> 0 <--> None
    print(l2) # 3 <--> 0 <--> None

