class LinkedList:
    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next = next


class Queue:

    def __init__(self) -> None:
        self.front = None
        self.rear = None
        self.count = 0

    def isEmpty(self) -> bool:
        return self.front == None

    def print(self) -> None:
        current = self.front
        while current:
            print(current.data, end=" ")
            current = current.next
        print(" ")

    def enqueue(self, data) -> None:
        node = LinkedList(data)

        if self.isEmpty():
            self.front = node
            self.rear = node
            self.count += 1

        else:
            if self.rear:
                self.rear.next = node
                self.rear = self.rear.next
                self.count += 1

    def dequeue(self) -> None:
        if self.front:
            self.front = self.front.next


if __name__ == "__main__":

    queue = Queue()

    array = [1, 2, 3, 4, 5, 6]

    for x in array:
        queue.enqueue(x)

    queue.print()

    queue.dequeue()

    queue.print()
