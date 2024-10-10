#question1
temp=[21,23,20,19,17,25,29]
print("temperature readings in 7days")
print("mon",temp[0],"tue",temp[1],"wed",temp[2], "thur",temp[3],"fri",temp[4],"sat",temp[5],"sun",temp[6],)
#question2
daily_sales=[1000,2400,1200,1700,1320,1400,1100]
avgsales=sum(daily_sales)/len(daily_sales)
print("average sales in the week is:",avgsales)
#question 3
stock_prices=[3,4,2,1,9,6,5,10,4]
minimum=min(stock_prices)
maximum=max(stock_prices)
print("mini",minimum,"max",maximum)
#qustion4
student_marks=[15,32,43,12,44,50,97,40]
student_marks.reverse()
print(student_marks)
#question5
import random
random_numbers = [random.randint(1, 100) for _ in range(40)]
even_count = 0
odd_count = 0
for num in random_numbers:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("random numbers:", random_numbers)
print("Number of even numbers:", even_count)
print("Number of odd numbers:", odd_count)
#question6
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]
    
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    
    return None

# Initialize a 3x3 tic-tac-toe board
board = [
    ["O", "O", "X"],
    ["O", "X", "O"],
    ["O", "X", "X"]
]

# Print the board
print_board(board)

# Check for a winner
winner = check_winner(board)
if winner:
    print(f"The winner is {winner}!")
else:
    print("No winner yet.")
#QUESTION7
# Initialize the 2D array with sales data
sales = [
    [150, 200, 250, 300, 350, 400, 450],  # Product 1 sales for each day
    [100, 150, 200, 250, 300, 350, 400],  # Product 2 sales for each day
    [50, 100, 150, 200, 250, 300, 350]    # Product 3 sales for each day
]

# Function to print the sales data
def print_sales(sales):
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    print("Product\t" + "\t".join(days))
    for i, product_sales in enumerate(sales):
        print(f"Product {i+1}\t" + "\t".join(map(str, product_sales)))

# Display the sales data
print_sales(sales)
#question8
import numpy as np

# Create a 2D array representing an RGB image (3 channels for Red, Green, Blue)
# For simplicity, let's create a 3x3 image with random values
image = np.random.randint(0, 256, (3, 3, 3), dtype=np.uint8)

print("Original Image:")
print(image)

# Invert the colors
inverted_image = 255 - image

print("\nInverted Image:")
print(inverted_image)

#question 9
# Initialize the 2D array with marks data
marks = [
    [85, 90, 78],  # Student 1 marks in 3 subjects
    [88, 76, 92],  # Student 2 marks in 3 subjects
    [79, 85, 88]   # Student 3 marks in 3 subjects
]

# Function to calculate total marks for each student
def calculate_total_marks(marks):
    total_marks = []
    for student_marks in marks:
        total_marks.append(sum(student_marks))
    return total_marks

# Calculate total marks for each student
total_marks = calculate_total_marks(marks)

# Print the total marks
for i, total in enumerate(total_marks):
    print(f"Total marks for Student {i+1}: {total}")
#question10
    
import numpy as np

# Create a 3D array with dimensions (4 cities x 7 days x 1 temperature reading per day)
temperatures = np.array([
    [ [30, 32, 31, 29, 28, 30, 31],  # City 1
      [25, 26, 27, 28, 29, 30, 31],  # City 2
      [20, 21, 22, 23, 24, 25, 26],  # City 3
      [15, 16, 17, 18, 19, 20, 21]   # City 4
    ]
])

# Calculate the average temperature for each city
average_temperatures = np.mean(temperatures, axis=1)

# Print the average temperatures
cities = ["City 1", "City 2", "City 3", "City 4"]
for i, avg_temp in enumerate(average_temperatures):
    print(f"Average temperature for {cities[i]}: {avg_temp}°C")

#practical exercises for list

#question1
# List of names of people who attended the meeting
attendees = ["Alice", "Bob", "Charlie", "Diana"]

print("Original list of attendees:")
print(attendees)

# Add a new name to the list
new_attendee = "Eve"
attendees.append(new_attendee)

print("\nUpdated list of attendees:")
print(attendees)
#question2
# Create a shopping list
shopping_list = ["milk", "eggs", "bread", "butter", "cheese"]

print("Original shopping list:")
print(shopping_list)

# Remove an item from the list
item_to_remove = "bread"
shopping_list.remove(item_to_remove)

print("\nUpdated shopping list:")
print(shopping_list)
#question3
# List of ages
ages = [34, 23, 45, 22, 36, 29]

print("Original list of ages:")
print(ages)

# Sort the list in ascending order
ages.sort()

print("\nSorted list of ages:")
print(ages)
#question4
# Create a to-do list
to_do_list = ["Finish homework", "Clean the house", "Buy groceries", "Call mom"]

print("Original to-do list:")
print(to_do_list)

# Mark a task as completed by removing it from the list
completed_task = "Buy groceries"
to_do_list.remove(completed_task)

print("\nUpdated to-do list:")
print(to_do_list)
#question5
friends_list1 = ["Alice", "Bob", "Charlie", "Diana"]
friends_list2 = ["Eve", "Frank", "Charlie", "Alice"]

print("List 1:")
print(friends_list1)

print("\nList 2:")
print(friends_list2)

# Merge the two lists and remove duplicates
merged_list = list(set(friends_list1 + friends_list2))

print("\nMerged list without duplicates:")
print(merged_list)
#question6
# List of lists containing the name, age, and grade of students
students = [
    ["Alice", 20, 85],
    ["Bob", 22, 90],
    ["Charlie", 21, 88],
    ["Diana", 23, 92],
    ["Eve", 20, 87]
]

print("Original list of students:")
for student in students:
    print(student)

# Sort the list by grade
students.sort(key=lambda x: x[2])

print("\nSorted list of students by grade:")
for student in students:
    print(student)

#question7
import numpy as np

# Define the categories and the expenses for 6 months
categories = ["Rent", "Food", "Utilities", "Transportation", "Entertainment"]
expenses = [
    [1200, 1300, 1250, 1280, 1220, 1270],  # Rent
    [300, 320, 310, 305, 315, 325],        # Food
    [150, 160, 155, 158, 152, 157],        # Utilities
    [100, 110, 105, 108, 102, 107],        # Transportation
    [200, 220, 210, 215, 205, 225]         # Entertainment
]

# Convert the list to a NumPy array for easier calculations
expenses_array = np.array(expenses)

# Calculate the average monthly expense per category
average_expenses = np.mean(expenses_array, axis=1)

# Print the results
print("Average monthly expenses per category:")
for category, avg_expense in zip(categories, average_expenses):
    print(f"{category}: ${avg_expense:.2f}")

#question8
# Create a 2D list representing the seating arrangement in a theater
# Let's assume a small theater with 5 rows and 6 seats per row
seating_arrangement = [
    ["A1", "A2", "A3", "A4", "A5", "A6"],
    ["B1", "B2", "B3", "B4", "B5", "B6"],
    ["C1", "C2", "C3", "C4", "C5", "C6"],
    ["D1", "D2", "D3", "D4", "D5", "D6"],
    ["E1", "E2", "E3", "E4", "E5", "E6"]
]

print("Original seating arrangement:")
for row in seating_arrangement:
    print(row)

# Assign reserved seats
reserved_seats = ["A1", "B3", "C5", "D2", "E6"]

# Mark reserved seats with an 'R'
for row in seating_arrangement:
    for i in range(len(row)):
        if row[i] in reserved_seats:
            row[i] = "R"

print("\nSeating arrangement with reserved seats:")
for row in seating_arrangement:
    print(row)

#question9
# List of lists containing product details (name, price, stock)
products = [
    ["Laptop", 1200, 10],
    ["Smartphone", 800, 0],
    ["Tablet", 300, 5],
    ["Headphones", 150, 0],
    ["Smartwatch", 200, 7]
]

print("Original list of products:")
for product in products:
    print(product)

# Filter out products that are out of stock
in_stock_products = [product for product in products if product[2] > 0]

print("\nList of products in stock:")
for product in in_stock_products:
    print(product)

#question10
# List of lists containing the scores of different games played in a tournament
# Each sublist represents a player and their scores in different games
scores = [
    ["Alice", [85, 90, 78]],
    ["Bob", [88, 92, 80]],
    ["Charlie", [90, 85, 85]],
    ["Diana", [92, 88, 84]],
    ["Eve", [78, 85, 88]]
]

print("Original list of scores:")
for player in scores:
    print(f"{player[0]}: {player[1]}")

# Calculate the average score for each player
for player in scores:
    player.append(sum(player[1]) / len(player[1]))

# Sort the list by average score in descending order
scores.sort(key=lambda x: x[2], reverse=True)

# Find the winner based on the highest average score
winner = scores[0]

print("\nSorted list of scores by average:")
for player in scores:
    print(f"{player[0]}: {player[1]}, Average: {player[2]:.2f}")

print(f"\nWinner: {winner[0]} with an average score of {winner[2]:.2f}")
