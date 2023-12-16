class Queue():
    def __init__(self, contents=[]):
        self.contents = contents

    def insert(self, item):
        self.contents.append(item)

    def remove(self):
        if len(self.contents) == 0:
            print("Queue is empty!")
        else:
            print(self.contents[0])
            self.contents = self.contents[1:]

my_queue = Queue()
my_queue.insert(5)
my_queue.insert(6)
my_queue.remove()
my_queue.insert(7)
my_queue.remove()
my_queue.remove()
my_queue.remove()

