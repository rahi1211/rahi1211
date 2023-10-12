# ## stack:-
#       stack is a linear data structure
# stores itemes in a last-in/frist-out (lifo) or (filo) manner
#
# ex ap na books rahkhe 1,2,3,but ap pehle 3 uthao ga osko kehte lifo
#
# operatioins:
#
# 1,push:-incert an a elements
#
# 2 pop:-del an a elements(last element)
#
# 3 peak:-Display the last element
#
# 4.display:- display list

stack = []

while True:
    choice = int(input('''
    1. Push Element
    2. Pop Element
    3. Peek Element
    4. Display Stack
    5. Exit

    Enter your choice: '''))

    if choice == 1:
        item = input("Enter the value: ")
        stack.append(item)
        print("Item", item, "pushed onto the stack.")

    elif choice == 2:
        if len(stack) == 0:
            print("Empty stack. Cannot pop.")
        else:
            popped_item = stack.pop()
            print("Popped item:", popped_item)

    elif choice == 3:
        if len(stack) == 0:
            print("Empty stack. No item to peek at.")
        else:
            print("Top element of the stack:", stack[-1])

    elif choice == 4:
        print("Stack:", stack)

    elif choice == 5:
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please select a valid option.")



