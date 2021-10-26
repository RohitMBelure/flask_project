from flask import Flask, request, make_response, redirect, abort
app = Flask(__name__)

def load_user(dev):
	return 'dev is a nice guy!!'

@app.route('/')
def index():
	user_agent = request.headers.get('User-Agent')
	return '<p>Your browser is %s</p>' %user_agent

@app.route('/bad')
def bad():
	return '<h1>Bad Request</h1>', 400

@app.route('/response')
def response():
	response = make_response('<h1>This document carries a cookie!</h1>')
	response.set_cookie('answer', '42')
	return response

@app.route('/home')
def home():
	return redirect('http://127.0.0.1:5000/')

@app.route('/user/<id>')
def get_user(id):
	user = load_user(id)
	if not user:
		abort(404)
	return '<h1>Hello, %s!</h1>' % user

if __name__ == '__main__':
	app.run(debug=True)









