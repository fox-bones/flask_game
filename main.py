from flask import Flask, render_template, request, redirect, session
import string
import random

app = Flask(__name__)
app.config['DEBUG'] = True
app.secret_key = 'SIH*v-6u)c>q<;;h&);cRw,1E_CO8>'

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        message = ''
        computer_choice = random.randint(1, 5)
        choice = request.form['choice']
        player_choice_message = ''
        computer_choice_message = ''
        winning_message = ''
        # handling player rock choice
        if choice == 'rock' and computer_choice == 2:
            message = 'Paper beats rock. Computer + 1'
            player_choice_message = 'You chose rock.'
            computer_choice_message = 'Computer chose paper.'
            session['computer_score'] += 1
        elif choice == 'rock' and computer_choice == 4:
            message = 'Dynamite beats rock. Computer + 1'
            player_choice_message = 'You chose rock.'
            computer_choice_message = 'Computer chose dynamite.'
            session['computer_score'] += 1
        elif choice == 'rock' and computer_choice == 3:
            message = 'Rock beats scissors. Player + 1'
            player_choice_message = 'You chose rock.'
            computer_choice_message = 'Computer chose scissors.'
            session['player_score'] += 1
        elif choice == 'rock' and computer_choice == 5:
            message = 'Rock beats drill. Player + 1'
            player_choice_message = 'You chose rock.'
            computer_choice_message = 'Computer chose drill.'
            session['player_score'] += 1
        # handling player paper choice
        elif choice == 'paper' and computer_choice == 3:
            message = 'Scissors beat paper. Computer + 1'
            player_choice_message = 'You chose paper.'
            computer_choice_message = 'Computer chose scissors.'
            session['computer_score'] += 1
        elif choice == 'paper' and computer_choice == 5:
            message = 'Drill beats paper. Computer + 1'
            player_choice_message = 'You chose paper.'
            computer_choice_message = 'Computer chose drill.'
            session['computer_score'] += 1
        elif choice == 'paper' and computer_choice == 4:
            message = 'Paper beats dynamite. Player + 1'
            player_choice_message = 'You chose paper.'
            computer_choice_message = 'Computer chose dynamite.'
            session['player_score'] += 1
        elif choice == 'paper' and computer_choice == 1:
            message = 'Paper beats rock. Player + 1'
            player_choice_message = 'You chose paper.'
            computer_choice_message = 'Computer chose rock.'
            session['player_score'] += 1
        # handling player scissors choice
        elif choice == 'scissors' and computer_choice == 5:
            message = 'Drill beats scissors. Computer + 1'
            player_choice_message = 'You chose scissors.'
            computer_choice_message = 'Computer chose dynamite.'
            session['computer_score'] += 1
        elif choice == 'scissors' and computer_choice == 1:
            message = 'Rock beats scissors. Computer + 1'
            player_choice_message = 'You chose scissors.'
            computer_choice_message = 'Computer chose rock.'
            session['computer_score'] += 1
        elif choice == 'scissors' and computer_choice == 4:
            message = 'Scissors beats dynamite. Player + 1'
            player_choice_message = 'You chose scissors.'
            computer_choice_message = 'Computer chose dynamite.'
            session['player_score'] += 1
        elif choice == 'scissors' and computer_choice == 2:
            message = 'Scissors beats paper. Player + 1'
            player_choice_message = 'You chose scissors.'
            computer_choice_message = 'Computer chose paper.'
            session['player_score'] += 1
        # handling player dynamite choice
        elif choice == 'dynamite' and computer_choice == 3:
            message = 'Scissors beats dynamite. Computer + 1'
            player_choice_message = 'You chose dynamite.'
            computer_choice_message = 'Computer chose scissors.'
            session['computer_score'] += 1
        elif choice == 'dynamite' and computer_choice == 2:
            message = 'Paper beats dynamite. Computer + 1'
            player_choice_message = 'You chose dynamite.'
            computer_choice_message = 'Computer chose paper.'
            session['computer_score'] += 1
        elif choice == 'dynamite' and computer_choice == 5: 
            message = 'Dynamite beats drill. Player + 1'
            player_choice_message = 'You chose dynamite.'
            computer_choice_message = 'Computer chose drill.'
            session['player_score'] += 1
        elif choice == 'dynamite' and computer_choice == 1:
            message = 'Dynamite beats rock. Player + 1'
            player_choice_message = 'You chose dynamite.'
            computer_choice_message = 'Computer chose rock.'
            session['player_score'] += 1
        # handling player drill choice
        elif choice == 'drill' and computer_choice == 1:
            message = 'Rock beats drill. Computer + 1'
            player_choice_message = 'You chose drill.'
            computer_choice_message = 'Computer chose rock.'
            session['computer_score'] += 1
        elif choice == 'drill' and computer_choice == 4:
            message = 'Dynamite beats drill. Computer + 1'
            player_choice_message = 'You chose drill.'
            computer_choice_message = 'Computer chose dynamite.'
            session['computer_score'] += 1
        elif choice == 'drill' and computer_choice == 3:
            message = 'Dill beats scissors. Player + 1'
            player_choice_message = 'You chose drill.'
            computer_choice_message = 'Computer chose scissors.'
            session['player_score'] += 1
        elif choice == 'drill' and computer_choice == 2:
            message = 'Drill beats paper. Player + 1'
            player_choice_message = 'You chose drill.'
            computer_choice_message = 'Computer chose paper.'
            session['player_score'] += 1
        else: 
            message = 'Draw!'
        if session['player_score'] == 5:
            winning_message = 'Player wins. Good job!'
            return render_template('play_again.html', winning_message = winning_message)
        if session['computer_score'] == 5:
            winning_message = 'Computer wins. Nice try!'
            return render_template('play_again.html', winning_message = winning_message)
        return render_template('index.html', message = message, player_choice_message = player_choice_message, computer_choice_message = computer_choice_message, player_score = session['player_score'], computer_score = session['computer_score'])
    elif request.method == 'GET':
        session['player_score'] = 0
        session['computer_score'] = 0
        player_choice_message = ''
        computer_choice_message = ''
        message = ''
        choice = ''
        return render_template('index.html')
    else:
        session['player_score'] = 0
        session['computer_score'] = 0
        message = ''
        choice = ''
        return render_template('index.html', message = message, choice = choice)

if __name__ == '__main__':
    app.run()