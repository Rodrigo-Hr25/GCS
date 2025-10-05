from flask import Flask, render_template, request, session
import random
import os

app = Flask(__name__)
app.secret_key = os.urandom(32)

current_number = 0


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate')
def generate():
    global current_number
    current_number = random.getrandbits(32)
    return {"CODE":"OK","NUMBER":current_number}

@app.route('/check', methods=['POST'])
def check():
    global current_number
    content = request.json
    if 'correct' in session:
        if content['attempt'] == current_number:
            session['correct'] += 1
            if session['correct'] == 10:
                    return {"CODE":"OK","FLAG":"CTFUA{cdab5a27-bc59-49c9-92b2-3dea9ddd7afb}"}
            return {"CODE":"OK","ANSWER":current_number}
    else:
        if content['attempt'] == current_number:
            session['correct'] = 1
            return {"CODE":"OK","ANSWER":current_number}
        else:
            session['correct'] = 0
    return {"CODE":"NOTOK","ANSWER":current_number}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

