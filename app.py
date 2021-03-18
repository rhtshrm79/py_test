from flask import Flask

app=Flask(__name__)

@app.route('/')
def hello():
	return "Hello! people.."

app.run(host='0.0.0.0')

