import tkinter as tk
import subprocess

def open_game_gui():
    # Code to open the game GUI with the board
    subprocess.Popen(["python", "game_gui.py"])

def open_qa_gui():
    # Code to open the question/answer GUI goes here
    subprocess.Popen(["python", "qa_gui.py"])

# Create a new window for the main interface
window = tk.Tk()

# Create a label for the main interface
label = tk.Label(window, text="Welcome to Trivial Compute", font=("Arial", 18))
label.pack(pady=20)

# Create buttons to navigate to the game GUI and QA GUI
game_button = tk.Button(window, text="Go to Game GUI", font=("Arial", 14), command=open_game_gui)
game_button.pack(pady=10)

qa_button = tk.Button(window, text="Go to QA GUI", font=("Arial", 14), command=open_qa_gui)
qa_button.pack(pady=10)

# Start the main event loop
window.mainloop()