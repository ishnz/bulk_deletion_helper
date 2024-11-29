import json
import os
from typing import Dict, List

def save_messages(messages: Dict[str, List[int]]):
	with open("messages.csv", "w", encoding='utf8') as f:
		f.write('channelid,messageid\n')
		for channel, ids in messages.items():
			if ids is None or len(ids) == 0:
				print(f'No messages found for channel: {channel} (skipping)')
				continue

			print(f'Saving messages from channel: {channel}')
			for id in ids:
				f.write(f'{channel},{id}\n')

def dump_dir(path: str) -> List[int]:
	messages = []
	if not os.path.isdir(path):
		return messages

	if not os.path.exists(f'{path}/messages.json'):
		print(f'No messages found in: {path}')
		return messages

	print(f'Dumping messages from: {path}')
	with open(f'{path}/messages.json', 'r', encoding='utf8') as f:
		messages_obj = json.load(f)
		for message in messages_obj:
			messages.append(message['ID'])

	return messages

def dump_all(blacklist: List[str]) -> Dict[str, List[int]]:
	messages = {}
	for channel in os.listdir('messages'):
		path = f'messages/{channel}'
		if not os.path.isdir(path):
			continue

		channel_id = channel.replace('c', '', 1)
		if channel_id in blacklist:
			print(f'Skipping channel: {channel_id} (in blacklist)')
			continue

		messages[channel_id] = dump_dir(path)

	return messages

def get_blacklist_channels():
	while True:
		file = input("Enter the text file containing the channel IDs to exclude:\n> ")
		if not os.path.exists(file):
			print("The path you entered does not exist.")
			continue

		if not os.path.isfile(file):
			print("The path you entered is not a file.")
			continue

		break

	with open(file, 'r', encoding='utf8') as f:
		lines = f.read().splitlines()
		lines = list(set([line.strip() for line in lines if line.strip()]))

	return lines

def main():
	blacklist = get_blacklist_channels()
	messages = dump_all(blacklist)
	save_messages(messages)

if __name__ == "__main__":
	main()
	print("Dumped to messages.csv!")