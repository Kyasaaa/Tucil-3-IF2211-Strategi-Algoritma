class PriorityQueue:
    # Constructor
    def __init__(self):
        self.queue = []

    # Check if PriorityQueue is empty
    def is_empty(self):
        return len(self.queue) == 0

    # Push puzzle_info to PQ 
    def enqueue(self, puzzle_info):
        pos = 0
        while(pos < len(self.queue) and puzzle_info[0] + puzzle_info[1] > self.queue[pos][0] + self.queue[pos][1]):
            pos += 1    
        self.queue.insert(pos, puzzle_info)
    
    # Remove first element of PQ
    def dequeue(self):
        if (self.is_empty()):
            print("Priority Queue kosong")
        else:
            return self.queue.pop(0)