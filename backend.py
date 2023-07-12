from flask import Flask, request
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'your_username'
app.config['MYSQL_PASSWORD'] = 'your_password'
app.config['MYSQL_DB'] = 'your_database_name'

mysql = MySQL(app)

@app.route('/', methods=['POST'])
def process_data():
    data = request.get_json()

    # Process the received data
    player_names = data['player_names']
    player_colors = data['player_colors']
    categories = data['categories']
    questions = data['questions']
    answers = data['answers']

    # Store player names and colors in the database
    for player_name, color in player_colors.items():
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO players (name, color) VALUES (%s, %s)", (player_name, color))
        mysql.connection.commit()
        cur.close()

    # Get the player IDs from the database
    player_ids = {}
    cur = mysql.connection.cursor()
    for player_name in player_names:
        cur.execute("SELECT id FROM players WHERE name = %s", (player_name,))
        result = cur.fetchone()
        player_ids[player_name] = result[0]
    cur.close()

    # Store categories, questions, and answers in the database
    for category, question, answer in zip(categories, questions, answers):
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO qa_data (category, question, answer) VALUES (%s, %s, %s)", (category, question, answer))
        question_id = cur.lastrowid
        mysql.connection.commit()
        cur.close()

        # Store player answers in the database
        for player_name, player_id in player_ids.items():
            player_answer = request.form.get(f"{player_name}_{question_id}")
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO player_answers (player_id, question_id, answer) VALUES (%s, %s, %s)", (player_id, question_id, player_answer))
            mysql.connection.commit()
            cur.close()

    # Return a response if needed
    return 'Data received and stored successfully'

if __name__ == '__main__':
    app.run()
