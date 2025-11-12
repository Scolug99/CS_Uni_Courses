# Python Crash Course Result

def greet_user(uname):
	if (uname == 'Jack'):
		print('Howdy', uname)
	else:
		print('Hallo', uname)
	
counter = 0
while counter < 5:
	username = input('Enter your name!')
	greet_user(username)
	counter = counter + 1
