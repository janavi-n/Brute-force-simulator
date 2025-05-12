from flask import Flask, render_template, request, redirect, url_for, session
import string
import time
import itertools
import uuid

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Needed for session

# Global in-memory dictionary to store guesses
global_guesses = {}

def brute_force(password):
    characters = string.ascii_lowercase + string.digits
    guesses = []
    attempts = 0

    # Set the maximum password length to 4
    max_length = 4

    # Truncate the password to 4 characters if it's longer
    password = password[:max_length]

    start_time = time.time()

    # Brute force with 1 to 4 characters, not necessarily 4
    for length in range(1, max_length + 1):
        for guess_tuple in itertools.product(characters, repeat=length):
            guess = ''.join(guess_tuple)
            guesses.append(guess)
            attempts += 1
            if guess == password:
                break

    time_taken = time.time() - start_time
    return True, attempts, round(time_taken, 4), guesses

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_attack', methods=['POST'])
def start_attack():
    password = request.form['password']
    if not password or len(password) > 4:
        return "Password must be between 1 and 4 characters.", 400

    found, attempts, time_taken, guesses = brute_force(password)

    # Generate a unique session ID
    sid = str(uuid.uuid4())
    session['sid'] = sid
    session['password'] = password
    session['attempts'] = attempts
    session['time_taken'] = time_taken

    # Store guesses in global memory
    global_guesses[sid] = guesses

    return redirect(url_for('guesses'))

@app.route('/guesses', methods=['GET'])
def guesses():
    sid = session.get('sid')
    guesses = global_guesses.get(sid, [])
    total_guesses = len(guesses)
    per_page = 100  # Show 100 guesses per page
    page = int(request.args.get('page', 1))  # Default to page 1

    # Calculate the starting and ending index for the current page
    start = (page - 1) * per_page
    end = start + per_page
    current_guesses = guesses[start:end]

    # Calculate the total number of pages
    total_pages = (total_guesses // per_page) + (1 if total_guesses % per_page > 0 else 0)

    return render_template(
        'guesses.html',
        guesses=current_guesses,
        attempts=session.get('attempts', 0),
        time_taken=session.get('time_taken', 0),
        password=session.get('password', '???'),
        page=page,
        total_pages=total_pages
    )

if __name__ == '__main__':
    app.run(debug=True)
