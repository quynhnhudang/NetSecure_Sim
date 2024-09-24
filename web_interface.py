from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/start_scenario', methods=['POST'])
def start_scenario():
    scenario_id = request.form['scenario_id']
    os.system(f'python scenario_{scenario_id}.py')
    return 'Scenario started'

if __name__ == '__main__':
    app.run(debug=True)
