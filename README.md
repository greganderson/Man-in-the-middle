Man-In-The-Middle Attack Tester
===============================

A simple client/server package to practice the man-in-the-middle attack.


Required packages
=================

Both can be gotten with pip (if you don't have pip, upgrade your python version
to the latest version (it comes with pip (one of the best things to happen to
python ever))):
	- Requests
	- Flask

server.py: A simple server that is listening for a message, prints the message,
then returns the message to the client.

client.py: A simple client that asks the user for a message, sends the message
to the server, then prints the response text.  The client will ask for messages
forever until the user presses Ctrl-c.


To run
======

Pull up two terminal windows.  In one window, run:
python server.py

In the other window, run:
python client.py

The client window should then be asking for messages, so you are set to go!

Author
======

Greg Anderson
