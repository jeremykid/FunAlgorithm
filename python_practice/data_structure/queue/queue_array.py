class queue_array():
    def __init__(self, length = 10): 
        self.array = [None]*length
        self.index = 0

    def __str__(self):
        output = ""
        for i in range(len(self.array)):
            if (self.array[i]):
                output += str(self.array[i]) + " -> "
        output += " End "
        return output

    def enqueue(self, value):
        if (self.full()):
            return "queue Full"
        self.array[self.index] = value
        self.index += 1 


    def dequeue(self):
        if (self.empty()):
            return "queue empty"
        self.index -= 1 
        result = self.array[0]
        for i in range(len(self.array)-1):
            self.array[i] = self.array[i+1]
        return result

    def empty(self):
        return (self.index == 0)

    def full(self):
        return (len(self.array) == self.index)