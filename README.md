# Flask Brute Force Simulator

A simple Flask web application that demonstrates how brute-force attacks can be used to guess short passwords (1 to 4 characters long) using lowercase letters and digits.

## Problem Statement

The purpose of this project is to simulate a brute-force attack on a short password. Users input a password (up to 4 characters), and the application will attempt to guess it using brute-force methods.

## Setup Instructions

1. Install dependencies:
```bash
pip install flask
```

2. Run the application:
```bash
python app.py
```

3. Open a browser and go to `http://127.0.0.1:5000`.

## Sample Logs

```
 * Running on http://127.0.0.1:5000
127.0.0.1 - - [DATE] "GET / HTTP/1.1" 200 -
127.0.0.1 - - [DATE] "POST /start_attack HTTP/1.1" 302 -
127.0.0.1 - - [DATE] "GET /guesses?page=1 HTTP/1.1" 200 -
```

## License

MIT License

## Disclaimer

This project is for **educational purposes only**. Do not use this technique on unauthorized systems.
