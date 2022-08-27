# Basic stack program
print("\t\t***Basic Stack***")
data = []
# enqueue
data.append(5)  # push method
data.append(10)
data.append(8)
data.append(11)

print("Current List: ", data)

# Basic Queue using a list
# Dequeue
print("\n\t\t***Basic Queue***")
data.pop(0)  # removes left-hand side
element = data.pop(0)
print("Element popped: ", element)
print("Current List: ", data)
