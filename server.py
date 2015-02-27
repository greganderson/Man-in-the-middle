from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
	return "Hello, World!"

@app.route('/<user_message>', methods=['GET'])
def message(user_message):
	print user_message
	return user_message

if __name__ == '__main__':
	app.run(debug=True)
