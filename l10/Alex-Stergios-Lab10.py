# -----------------------------------------------------
# CSCI 127, Lab 10                                    |
# Date                                  |
# Your Name                                           |
# -----------------------------------------------------

# Your solution goes here.  Do not change anything below.
class Queue:
    
    def __init__(self, init_name):
        name = init_name
        self.line = []
        
    
    
    def enqueue(self, number):        
        self.line.append(number)
        
        return self.line
        
    
    
    def dequeue(self):
        return self.line.pop(0)
        
        
    
    
    def is_empty(self):
        if len(self.line) == 0:
            return True
        else:
            return False
 
    def __str__(self):
                
        answer = "Contents: "
        for i in range(len(self.line)):
            answer += str(self.line[i])
            answer += " "
        
        
        return answer
    
    
    
    #magic idk
    def __iadd__(self, other):
        # self.line.append(other)
        # return self.line        
        
        self.line.append(other)
        answer = "Contents: "
        for i in range(len(self.line)):
            answer += str(self.line[i])
            answer += " "
        
        return answer
            
            
        
        
        
    
    
    
# -----------------------------------------------------

def main():
    numbers = Queue("Numbers")

    print("Enqueue 1, 2, 3, 4, 5")
    print("---------------------")
    for number in range(1, 6):
        numbers.enqueue(number)
        print(numbers)

    print("\nDequeue one item")
    print("----------------")
    numbers.dequeue()
    print(numbers)

    print("\nDeque all items")
    print("---------------")
    while not numbers.is_empty():
        print("Item dequeued:", numbers.dequeue())
        print(numbers)

    # Enqueue 10, 11, 12, 13, 14
    for number in range(10, 15):
        numbers.enqueue(number)

    # Enqueue 15
    numbers += 15

    print("\n10, 11, 12, 13, 14, 15 enqueued")
    print("-------------------------------")
    print(numbers)

# -----------------------------------------------------

main()