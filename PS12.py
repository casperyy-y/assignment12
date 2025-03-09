# Dynamic List Processing Assignment

# Step 1: Create a list with user-defined length
num_items = int(input("Enter the number of items in the list: "))
num_list = []  # Initialize empty list

for _ in range(num_items):
    num = int(input("Enter an integer: "))
    num_list.append(num)

print("Initial List:", num_list)

# Step 2: Insert 99 at position 1
num_list.insert(1, 99)
print("List after inserting 99 at position 1:", num_list)

# Step 3: Replace 99 with 100
index_99 = num_list.index(99)  # Find the index of 99
num_list[index_99] = 100
print("List after replacing 99 with 100:", num_list)

# Step 4: Create second list and extend first list
second_list = [500, 600, 700, 800, 900]
print("Second List:", second_list)

num_list.extend(second_list)
print("List after extending with second list:", num_list)

# Step 5: Remove value 800
if 800 in num_list:
    num_list.remove(800)
print("List after removing 800:", num_list)

# Step 6: Remove third item (index 2)
if len(num_list) > 2:
    del num_list[2]
print("List after removing third item:", num_list)

# Step 7: Create list of grades
grades = ["A", "B", "C", "A", "A", "C"]
print("Grades List:", grades)

# Step 8: Count occurrences of 'A'
count_A = grades.count("A")
print("Number of 'A' grades:", count_A)

# Step 9: Find index of first 'B'
if "B" in grades:
    index_B = grades.index("B")
    print("Index of first 'B' grade:", index_B)

# Step 10: Check if 'F' is in the list
if "F" not in grades:
    print("Grade 'F' is not in the list.")

# Step 11: Clear second list
second_list.clear()
print("Second list after clearing:", second_list)

# Step 12: Delete second list and try displaying it
del second_list
try:
    print(second_list)  # This will cause an error
except NameError:
    print("Error: second_list no longer exists.")

# Step 13: Create and sort list of players
players = ["Rizzo", "Davis", "Baez", "Happ", "Bryan"]
players.sort()
print("Sorted Players List:", players)

# Step 14: Copy players list into players2
players2 = players.copy()
print("Copied Players List (players2):", players2)

# Step 15: Reverse players2
players2.reverse()
print("Original Players List:", players)
print("Reversed Players2 List:", players2)
