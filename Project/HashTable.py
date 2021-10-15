
INITIAL_CAPACITY = 41

class HashValue:
    def __init__(self, value):
        self.value = value
        self.next = None

class HashTable:
    def __init__(self):
        self.__capacity = INITIAL_CAPACITY
        self.__list = [None] * self.__capacity
        self.__size = 0

    def hash(self, value):
        asciiSum = 0
        for i in range(len(value)):
            asciiSum += ord(value[i])
        return asciiSum % INITIAL_CAPACITY

    def add(self, value):
        self.__size += 1
        index = self.hash(value)

        hv = self.__list[index]

        if hv is None:
            self.__list[index] = HashValue(value)
            return

        prev = hv
        while hv is not None:
            prev = hv
            hv = hv.next

        prev.next = HashValue(value)

    def getId(self, value):
        index = self.hash(value)

        hv = self.__list[index]

        while hv is not None and hv.value != value:
            hv = hv.next

        if hv is None:
            return None
        else:
            return hv.value

    def __str__(self):
        return str(self.__list)
