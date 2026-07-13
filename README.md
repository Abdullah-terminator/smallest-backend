Mini Backend

Description

A minimal backend server built with pure Python — no frameworks, no dependencies. Two JSON endpoints that demonstrate the request → response loop.

Prerequisites


Python 3 installed on your machine


Installation

No installation required. Just clone the repo and run.

bashgit clone https://github.com/YOUR_USERNAME/mini-backend.git
cd mini-backend

Usage

Start the Server

bashpython3 server.py

Server will start at http://localhost:3000

Stop the Server

Press Ctrl + C in the terminal.

Endpoints

GET /hello

bashcurl http://localhost:3000/hello

Response:

json{ "message": "Hello, World!" }

GET /about

bashcurl http://localhost:3000/about

Response:

json{
  "name": "Mini Backend",
  "author": "Abdullah",
  "university": "Air University"
}
