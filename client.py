import requests

try:
	while True:
		message = raw_input('Message: ')
		r = requests.get('http://localhost:5000/' + message)
		print r.text
except:
	print
	exit(0)
