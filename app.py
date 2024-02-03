from flask import Flask, render_template, jsonify
import subprocess
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_question')
def get_question():
    # Call C program to get the next question
    c_program_output = subprocess.check_output(['./quiz'], universal_newlines=True)
    
    # Parse the JSON-formatted question data
    question_data = json.loads(c_program_output)
    return jsonify(question_data)

@app.route('/submit_answer/<int:user_answer>')
def submit_answer(user_answer):
    # Call C program to check the user's answer
    c_program_output = subprocess.check_output(['./quiz', str(user_answer)], universal_newlines=True)
    
    # Parse the JSON-formatted result data
    result_data = json.loads(c_program_output)
    return jsonify(result_data)

if __name__ == '__main__':
    app.run(debug=True, port='8085')
