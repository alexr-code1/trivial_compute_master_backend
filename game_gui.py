import tkinter as tk
import random

# Function to highlight a cell in a specified color
def highlight_cell(row, col, color):
    x1 = 50 + (col - 1) * 300 / 9
    y1 = 50 + (row - 1) * 300 / 9
    x2 = x1 + 300 / 9
    y2 = y1 + 300 / 9
    canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="")

# Function to add text to a specific box
def add_text(row, col, text):
    x = 50 + (col - 0.5) * 300 / 9
    y = 50 + (row - 0.5) * 300 / 9
    cell_size = 300 / 9
    desired_text_size = cell_size * 0.95

    # Calculate the maximum font size that fits the desired percentage of the cell size
    max_font_size = 30
    font = ("Arial", max_font_size)
    text_width = canvas.create_text(0, 0, text=text, font=font, anchor="center", tags="temp_text")
    bbox = canvas.bbox(text_width)
    while bbox[2] - bbox[0] > desired_text_size or bbox[3] - bbox[1] > desired_text_size:
        max_font_size -= 1
        font = ("Arial", max_font_size)
        canvas.delete("temp_text")
        text_width = canvas.create_text(0, 0, text=text, font=font, anchor="center", tags="temp_text")
        bbox = canvas.bbox(text_width)

    # Remove the temporary text
    canvas.delete("temp_text")

    # Create the text with the adjusted font size
    canvas.create_text(x, y, text=text, font=font)

# Function to roll the dice
def roll_dice():
    number = random.randint(1, 6)
    roll_result.config(text=f"Dice Rolled: {number}")  # Update the roll result label

# Create a new window
window = tk.Tk()

# Create a canvas to draw the board
canvas = tk.Canvas(window, width=600, height=400)
canvas.pack()

# Highlight specific cells in red
highlight_cell(1, 5, "red")  # A5
highlight_cell(2, 1, "red")  # B1
highlight_cell(2, 9, "red")  # B9
highlight_cell(6, 1, "red")  # F1
highlight_cell(6, 9, "red")  # F9
highlight_cell(5, 4, "red")  # E4
highlight_cell(5, 8, "red")  # E8
highlight_cell(9, 3, "red")  # I3
highlight_cell(9, 7, "red")  # I7
highlight_cell(7, 5, "red")  # G5

# Highlight specific cells in green
highlight_cell(1, 4, "green")  # A4
highlight_cell(1, 8, "green")  # A8
highlight_cell(3, 1, "green")  # C1
highlight_cell(4, 5, "green")  # D5
highlight_cell(5, 3, "green")  # E3
highlight_cell(5, 9, "green")  # E9
highlight_cell(7, 1, "green")  # G1
highlight_cell(8, 5, "green")  # H5
highlight_cell(9, 4, "green")  # I4
highlight_cell(9, 8, "green")  # I8

# Highlight specific cells in yellow
highlight_cell(1, 2, "yellow")  # A2
highlight_cell(1, 6, "yellow")  # A6
highlight_cell(2, 5, "yellow")  # B5
highlight_cell(3, 9, "yellow")  # C9
highlight_cell(5, 1, "yellow")  # E1
highlight_cell(5, 7, "yellow")  # E7
highlight_cell(6, 5, "yellow")  # F5
highlight_cell(7, 9, "yellow")  # G9
highlight_cell(9, 2, "yellow")  # I2
highlight_cell(9, 6, "yellow")  # I6

# Highlight specific cells in very light grey (almost white)
highlight_cell(1, 1, "#f7f7f7")  # A1
highlight_cell(1, 9, "#f7f7f7")  # A9
highlight_cell(5, 5, "#f7f7f7")  # E5
highlight_cell(9, 1, "#f7f7f7")  # I1
highlight_cell(9, 9, "#f7f7f7")  # I9

# Highlight specific cells in blue
highlight_cell(1, 3, "blue")  # A3
highlight_cell(1, 7, "blue")  # A7
highlight_cell(3, 5, "blue")  # C5
highlight_cell(4, 1, "blue")  # D1
highlight_cell(4, 9, "blue")  # D9
highlight_cell(5, 2, "blue")  # E2
highlight_cell(5, 6, "blue")  # E6
highlight_cell(8, 1, "blue")  # H1
highlight_cell(8, 9, "blue")  # H9
highlight_cell(9, 5, "blue")  # I5

# Add text to specific cells
add_text(1, 5, "HQ")
add_text(5, 1, "HQ")
add_text(5, 9, "HQ")
add_text(9, 5, "HQ")

# Add text to specific cells with black color
add_text(1, 1, "Roll Again")
add_text(1, 9, "Roll Again")
add_text(5, 5, "Trivial Compute")
add_text(9, 1, "Roll Again")
add_text(9, 9, "Roll Again")

# Remove specific cells
remove_cells = [(2, 2), (2, 3), (2, 4), (2, 6), (2, 7), (2, 8),
                (3, 2), (3, 3), (3, 4), (3, 6), (3, 7), (3, 8),
                (4, 2), (4, 3), (4, 4), (4, 6), (4, 7), (4, 8),
                (6, 2), (6, 3), (6, 4), (6, 6), (6, 7), (6, 8),
                (7, 2), (7, 3), (7, 4), (7, 6), (7, 7), (7, 8),
                (8, 2), (8, 3), (8, 4), (8, 6), (8, 7), (8, 8)]

for cell in remove_cells:
    row, col = cell
    x = 50 + (col - 1) * 300 / 9
    y = 50 + (row - 1) * 300 / 9
    x2 = x + 300 / 9
    y2 = y + 300 / 9
    canvas.create_rectangle(x, y, x2, y2, fill="white", outline="")

# Add small boxes 25% away from the main grid
small_box_size = 75
small_box_x1 = 425
small_box_y1 = 100
small_box_x2 = small_box_x1 + small_box_size
small_box_y2 = small_box_y1 + small_box_size

canvas.create_rectangle(small_box_x1, small_box_y1, small_box_x2, small_box_y2, fill="white", outline="black")

small_box_x1 = 425
small_box_y1 = 225
small_box_x2 = small_box_x1 + small_box_size
small_box_y2 = small_box_y1 + small_box_size

canvas.create_rectangle(small_box_x1, small_box_y1, small_box_x2, small_box_y2, fill="white", outline="black")

# Create a label to display roll result
roll_result = tk.Label(window, text="Roll Result", font=("Arial", 16))
roll_result.pack(pady=10)

# Function to handle roll dice button click
def roll_dice_click():
    roll_dice()

# Create a button to roll the dice
roll_button = tk.Button(window, text="Roll Dice", font=("Arial", 14), command=roll_dice_click)
roll_button.pack(pady=10)

# Start the main event loop
window.mainloop()
