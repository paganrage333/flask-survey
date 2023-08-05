from flask import Flask, request, render_template, redirect, flash 
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

responses = []

@app.route('/')
def show_home():
    return render_template('home.html', survey=survey)

@app.route('/begin', methods=["POST"])
def begin_survey():
    return redirect('/questions/0')

@app.route('/answer')
def handle_question():
    choice = request.form['answer']

    responses.append(choice)

    if (len(responses) == len(survey.questions)):
        return redirect('/complete')
    else:
        return redirect(f"/questions/{len(responses)}")

@app.route('/questions/<int:qid>')
def show_question(qid):
    question = survey.questions[qid]
    return render_template('question.html', question_num=qid, question=question)


@app.route('/complete')
def complete():
    return render_template('complete.html')