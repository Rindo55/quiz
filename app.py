# app.py
from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

questions = [
    {"question": "Which bird lays the largest egg?", "options": ["Owl", "Ostrich", "Kingfisher", "Woodpecker"], "correct_option": 2},
    {"question": "How many legs does a spider have?", "options": ["7", "8", "6", "5"], "correct_option": 2},
    {"question": "Where does the President of the United States live while in office?", "options": ["The White House", "The Parliament", "House of Commons", "Washington DC"], "correct_option": 1},
    {"question": "Which state is famous for Hollywood?", "options": ["Sydney", "California", "New York", "Paris"], "correct_option": 2},
    {"question": "What is a group of lions called?", "options": ["Drift", "Pride", "Flock", "Drove"], "correct_option": 2}
]

@app.route('/')
def quiz():
    return render_template('index.html', questions=questions)

@app.route('/submit_quiz', methods=['POST'])
def submit_quiz():
    user_answers = [request.form.get(f'q{i + 1}', '') for i in range(len(questions))]
    c_program_command = 'chmod +x quiz6.exe'
    input_data = '\n'.join(user_answers)
    result, error_output = execute_c_program(c_program_command, input_data)

    print("Result from C program:", result)
    print("Error output from C program:", error_output)

    try:
        score, total_questions = map(int, result.strip().split())
    except (AttributeError, ValueError):
        # Handle the case where the result is not in the expected format
        score, total_questions = 0, len(questions)

    return render_template('result.html', score=score, total_questions=total_questions)

def execute_c_program(command, input_data):
    result = subprocess.run(command, shell=True, input=input_data.encode(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return result.stdout.decode('utf-8'), result.stderr.decode('utf-8')

if __name__ == '__main__':
    app.run(debug=True)
