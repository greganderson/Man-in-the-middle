import requests

ip = raw_input('Server IP (e.g. 192.168.1.17): ')

try:
	while True:
		message = raw_input('Message: ')
		r = requests.get(ip + ':5000/' + message)
		print r.text
except:
	print
	exit(0)
