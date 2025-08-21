# Implement a stack using a Python list to perform the following operations:

stack = []

# a. Push five elements onto the stack.
stack.append(10)
stack.append(20)
stack.append(30)
stack.append(40)
stack.append(50)

# b. Pop two elements from the stack.
stack.pop()
stack.pop()

# c. Check if the stack is empty.
if not stack:
    print("The stack is empty.")
else:
    print("The stack is not empty. Current elements:", stack)




# Implement a queue using a Python list to perform the following operations:

queue = []

# a. Enqueue five elements into the queue.
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)

# b. Dequeue three elements from the queue.
queue.pop(0)
queue.pop(0)
queue.pop(0)

# c. Check if the queue is empty.
if not queue:
    print("The queue is empty.")
else:
    print("The queue is not empty. Current elements:", queue)

