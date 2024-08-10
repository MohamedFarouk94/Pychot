OUTPUT_Q = []


def set_to_terminal(response):
	print(f'Received: {response}')


def set_to_queue(response):
	OUTPUT_Q.append(response)
	# print(f'"{response}" is appended successfully in OUTPUT_Q')
