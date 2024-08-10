import asyncio


INPUT_Q = []


def get_from_terminal():
	return input('Enter your message: ')


async def get_from_queue():
	while not INPUT_Q:
		await asyncio.sleep(0.1)
	# print("SOMETHING FOUND IN INPUT_Q")
	return INPUT_Q.pop(0)
