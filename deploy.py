from flask import Flask

app=Flask(__name__)

@app.route('/')
def index():
	return '<h1>Hello, This is Sanghamitra!!!</h1>'

