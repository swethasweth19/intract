from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # required for session management

questions = [
    "What's your superhero name if your favorite snack became your power?",
    "If animals could talk, which one would be the sassiest?",
    "What's the weirdest thing you’d name your pet?",
    "If you became invisible, what's the first silly thing you'd do?",
    "Which vegetable do you think has the most attitude?",
    "If your laugh had a sound effect, what would it be?",
    "Would you rather fight 1 horse-sized duck or 100 duck-sized horses?",
    "What's your secret talent that no one asked for?",
    "What’s the strangest thing you believed as a kid?",
    "What would you name a sandwich after yourself?",
    "If you had to speak in only movie quotes for a day, what’s your go-to line?",
    "What's your spirit emoji?",
    "If your life were a meme, what would the caption be?",
    "What’s something silly you’re irrationally afraid of?",
    "What’s your go-to dance move when no one's watching?"
]

@app.route('/', methods=['GET', 'POST'])
def index():
    if 'step' not in session:
        session['step'] = 0
        session['answers'] = []

    step = session['step']
    answers = session['answers']

    if request.method == 'POST':
        user_answer = request.form.get('answer')
        if user_answer:
            answers.append(user_answer)
            session['step'] = step + 1
            session['answers'] = answers

        if session['step'] >= len(questions):
            return redirect(url_for('thank_you'))

    if step < len(questions):
        question = questions[step]
        return render_template('index.html', question=question, step=step + 1, total=len(questions))

    return redirect(url_for('thank_you'))

@app.route('/thank-you')
def thank_you():
    return render_template('thank_you.html', answers=session.get('answers', []))

@app.route('/reset')
def reset():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5050,debug=True)
