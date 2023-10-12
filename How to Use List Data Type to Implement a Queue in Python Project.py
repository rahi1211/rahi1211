# the queue is a liner data structure

## stores itemes in frist in frist out (fifo) manner

## ex jisa ap relway sition py tackit book karen jate ho line hoti jo frist hota wo frist lega

## Queue opreation

# 1.engueue:ads an items to thr queue
## 2.dequeue:remove an item from queue
## 3.front:frist item
## 3.Rear get the last item from queue


queue = []

while True:
    choice = int(input('''
    1. Enqueue (Add an item to the queue)
    2. Dequeue (Remove an item from the queue)
    3. Front (Get the first item from the queue)
    4. Rear (Get the last item from the queue)
    5. Display Queue
    6. Exit

    Enter your choice: '''))

    if choice == 1:
        item = input("Enter the value: ")
        queue.append(item)
        print("Item", item, "added to the queue.")

    elif choice == 2:
        if len(queue) == 0:
            print("Empty queue. Cannot dequeue.")
        else:
            removed_item = queue.pop(0)
            print("Dequeued item:", removed_item)

    elif choice == 3:
        if len(queue) == 0:
            print("Empty queue. No item to get from the front.")
        else:
            print("Front element of the queue:", queue[0])

    elif choice == 4:
        if len(queue) == 0:
            print("Empty queue. No item to get from the rear.")
        else:
            print("Rear element of the queue:", queue[-1])

    elif choice == 5:
        print("Queue:", queue)

    elif choice == 6:
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please select a valid option.")





