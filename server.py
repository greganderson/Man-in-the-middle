from flask import Flask
import commands

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
	return "Hello world!"

@app.route('/<user_message>', methods=['GET'])
def message(user_message):
	print user_message
	return user_message

def get_network_ip():
	status, output = commands.getstatusoutput('ifconfig')

	o = output.split('\n')

	for line in o:
		if '192.168' in line:
			start = line[line.find('192.168'):]
			return start[:start.find(' ')]

if __name__ == '__main__':
	print 'Network IP: ' + get_network_ip()
	app.run(host='0.0.0.0')
