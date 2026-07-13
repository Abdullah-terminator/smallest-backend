# smallest-backend
My first backend! A simple server with two JSON endpoints.
Mini Backend (Python)

A minimal backend server with two JSON endpoints. No frameworks, no dependencies — pure Python.

Run

bashpython3 server.py

Endpoints

GET /hello

bashcurl http://localhost:3000/hello

json{ "message": "Hello, World!" }

GET /about

bashcurl http://localhost:3000/about

json{ "name": "Mini Backend", "author": "Abdullah", "university": "Air University" }

Stop the server

Press Ctrl + C in the terminal.
