class Deque:
    def __init__(self):
        self.items = []
    def addfront(self, item): #enqueueToHead
        self.items.insert(0, item)
    def addrear(self, item): #enqueueToTail
        self.items.append(item)
    def removefront(self): #dequeueFromHead
        if self.isempty():
            return None
        return self.items.pop(0)
    def removerear(self): #dequeueFromTail
        if self.isempty():
            return None
        return self.items.pop()
    def isempty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)
    def print_dequeue(self):
        print(self.items)
def main():
    deques = Deque()
    deques.addfront(1)
    deques.addfront(2)
    deques.addfront(3)
    deques.addrear(4)
    deques.addrear(5)
    deques.removefront()
    deques.removerear()
    print("Deque:")
    deques.print_dequeue()
main()