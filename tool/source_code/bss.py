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
                time_taken = time.time() - start_time
                return True, attempts, round(time_taken, 4), guesses

    time_taken = time.time() - start_time
    return False, attempts, round(time_taken, 4), guesses
