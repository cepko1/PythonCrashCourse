def send_message(input_messages, output_messages):
	while input_messages:
		message = input_messages.pop()
		print(f'Message "{message}" is sending')
		output_messages.append(message)
def show_message(messages):
	for message in messages:
		print(f'Message {message}')
		
input_messages = ['Hello', 'achtung', 'bye', 'test']
output_messages = []
send_message(input_messages[:], output_messages)
show_message(input_messages)
show_message(output_messages)