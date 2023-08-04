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

@app.route('/questions/<int:qid>')
def show_question(qid):
    question = survey.questions[qid]
    return render_template('question.html', question_num=qid, question=question)