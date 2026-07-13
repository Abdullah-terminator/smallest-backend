Mini Backend
Two JSON endpoints — pure Python, zero dependencies

No frameworks · No install · ~20 lines
About
Author — Abdullah
University — Air University, Kamra
Language — Python 3 (built-in http.server)
Port — localhost:3000
Run it
1
Clone or download the repo, then open a terminal in the project folder.
2
Start the server: python3 server.py
3
Open your browser or use curl to hit an endpoint. Stop with Ctrl + C.
Endpoints
GET
/hello
curl http://localhost:3000/hello
{ "message": "Hello, World!" }
GET
/about
curl http://localhost:3000/about
{ "name": "Mini Backend", "author": "Abdullah", "university": "Air University" }
