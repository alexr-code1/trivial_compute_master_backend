import tkinter as tk
import requests
import json

def submit_details():
    category1 = category_entry1.get()
    category2 = category_entry2.get()
    category3 = category_entry3.get()
    category4 = category_entry4.get()

    player1_name = player_entry1.get()
    player2_name = player_entry2.get()
    player3_name = player_entry3.get()
    player4_name = player_entry4.get()

    player1_color = color_var1.get()
    player2_color = color_var2.get()
    player3_color = color_var3.get()
    player4_color = color_var4.get()

    player_colors = {
        player1_name: player1_color,
        player2_name: player2_color,
        player3_name: player3_color,
        player4_name: player4_color
    }

    categories = [category1, category2, category3, category4]
    questions = [question_entry1.get(), question_entry2.get(), question_entry3.get(), question_entry4.get()]
    answers = [answer_entry1.get(), answer_entry2.get(), answer_entry3.get(), answer_entry4.get()]

    data = {
        'player_names': [player1_name, player2_name, player3_name, player4_name],
        'player_colors': player_colors,
        'categories': categories,
        'questions': questions,
        'answers': answers
    }

    # Send data to the Flask backend
    url = 'http://localhost:5000/'  # Replace with the correct backend URL
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=json.dumps(data), headers=headers)

    # Process the response if needed
    if response.status_code == 200:
        print('Data sent successfully')
    else:
        print('Error:', response.text)

# Create a new window for the question/answer GUI
qa_window = tk.Tk()
qa_window.title("QA GUI")

# Create labels and entry fields for categories
category_label1 = tk.Label(qa_window, text="Category 1:")
category_label1.pack()
category_entry1 = tk.Entry(qa_window)
category_entry1.pack()

category_label2 = tk.Label(qa_window, text="Category 2:")
category_label2.pack()
category_entry2 = tk.Entry(qa_window)
category_entry2.pack()

category_label3 = tk.Label(qa_window, text="Category 3:")
category_label3.pack()
category_entry3 = tk.Entry(qa_window)
category_entry3.pack()

category_label4 = tk.Label(qa_window, text="Category 4:")
category_label4.pack()
category_entry4 = tk.Entry(qa_window)
category_entry4.pack()

# Create labels and entry fields for player names
player_label1 = tk.Label(qa_window, text="Player 1 Name:")
player_label1.pack()
player_entry1 = tk.Entry(qa_window)
player_entry1.pack()

player_label2 = tk.Label(qa_window, text="Player 2 Name:")
player_label2.pack()
player_entry2 = tk.Entry(qa_window)
player_entry2.pack()

player_label3 = tk.Label(qa_window, text="Player 3 Name:")
player_label3.pack()
player_entry3 = tk.Entry(qa_window)
player_entry3.pack()

player_label4 = tk.Label(qa_window, text="Player 4 Name:")
player_label4.pack()
player_entry4 = tk.Entry(qa_window)
player_entry4.pack()

# Create radio buttons for player colors
color_frame = tk.Frame(qa_window)
color_frame.pack()

color_label1 = tk.Label(color_frame, text="Select Player 1 Color:")
color_label1.grid(row=0, column=0, padx=5, pady=5)
color_var1 = tk.StringVar(value="blue")
color_rb1_blue = tk.Radiobutton(color_frame, text="Blue", variable=color_var1, value="blue")
color_rb1_blue.grid(row=0, column=1)

color_rb1_green = tk.Radiobutton(color_frame, text="Green", variable=color_var1, value="green")
color_rb1_green.grid(row=0, column=2)

color_rb1_red = tk.Radiobutton(color_frame, text="Red", variable=color_var1, value="red")
color_rb1_red.grid(row=0, column=3)

color_rb1_yellow = tk.Radiobutton(color_frame, text="Yellow", variable=color_var1, value="yellow")
color_rb1_yellow.grid(row=0, column=4)

color_label2 = tk.Label(color_frame, text="Select Player 2 Color:")
color_label2.grid(row=1, column=0, padx=5, pady=5)
color_var2 = tk.StringVar(value="blue")
color_rb2_blue = tk.Radiobutton(color_frame, text="Blue", variable=color_var2, value="blue")
color_rb2_blue.grid(row=1, column=1)

color_rb2_green = tk.Radiobutton(color_frame, text="Green", variable=color_var2, value="green")
color_rb2_green.grid(row=1, column=2)

color_rb2_red = tk.Radiobutton(color_frame, text="Red", variable=color_var2, value="red")
color_rb2_red.grid(row=1, column=3)

color_rb2_yellow = tk.Radiobutton(color_frame, text="Yellow", variable=color_var2, value="yellow")
color_rb2_yellow.grid(row=1, column=4)

color_label3 = tk.Label(color_frame, text="Select Player 3 Color:")
color_label3.grid(row=2, column=0, padx=5, pady=5)
color_var3 = tk.StringVar(value="blue")
color_rb3_blue = tk.Radiobutton(color_frame, text="Blue", variable=color_var3, value="blue")
color_rb3_blue.grid(row=2, column=1)

color_rb3_green = tk.Radiobutton(color_frame, text="Green", variable=color_var3, value="green")
color_rb3_green.grid(row=2, column=2)

color_rb3_red = tk.Radiobutton(color_frame, text="Red", variable=color_var3, value="red")
color_rb3_red.grid(row=2, column=3)

color_rb3_yellow = tk.Radiobutton(color_frame, text="Yellow", variable=color_var3, value="yellow")
color_rb3_yellow.grid(row=2, column=4)

color_label4 = tk.Label(color_frame, text="Select Player 4 Color:")
color_label4.grid(row=3, column=0, padx=5, pady=5)
color_var4 = tk.StringVar(value="blue")
color_rb4_blue = tk.Radiobutton(color_frame, text="Blue", variable=color_var4, value="blue")
color_rb4_blue.grid(row=3, column=1)

color_rb4_green = tk.Radiobutton(color_frame, text="Green", variable=color_var4, value="green")
color_rb4_green.grid(row=3, column=2)

color_rb4_red = tk.Radiobutton(color_frame, text="Red", variable=color_var4, value="red")
color_rb4_red.grid(row=3, column=3)

color_rb4_yellow = tk.Radiobutton(color_frame, text="Yellow", variable=color_var4, value="yellow")
color_rb4_yellow.grid(row=3, column=4)

# Create labels and entry fields for questions and answers
question_label1 = tk.Label(qa_window, text="Question 1:")
question_label1.pack()
question_entry1 = tk.Entry(qa_window)
question_entry1.pack()

answer_label1 = tk.Label(qa_window, text="Answer 1:")
answer_label1.pack()
answer_entry1 = tk.Entry(qa_window)
answer_entry1.pack()

question_label2 = tk.Label(qa_window, text="Question 2:")
question_label2.pack()
question_entry2 = tk.Entry(qa_window)
question_entry2.pack()

answer_label2 = tk.Label(qa_window, text="Answer 2:")
answer_label2.pack()
answer_entry2 = tk.Entry(qa_window)
answer_entry2.pack()

question_label3 = tk.Label(qa_window, text="Question 3:")
question_label3.pack()
question_entry3 = tk.Entry(qa_window)
question_entry3.pack()

answer_label3 = tk.Label(qa_window, text="Answer 3:")
answer_label3.pack()
answer_entry3 = tk.Entry(qa_window)
answer_entry3.pack()

question_label4 = tk.Label(qa_window, text="Question 4:")
question_label4.pack()
question_entry4 = tk.Entry(qa_window)
question_entry4.pack()

answer_label4 = tk.Label(qa_window, text="Answer 4:")
answer_label4.pack()
answer_entry4 = tk.Entry(qa_window)
answer_entry4.pack()

# Create a submit button to start the game with the entered details
submit_button = tk.Button(qa_window, text="Submit", command=submit_details)
submit_button.pack(pady=10)

# Start the question/answer GUI event loop
qa_window.mainloop()
