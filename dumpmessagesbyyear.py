import json
import os
from typing import Dict, List

def save_channels(messages: Dict[str, List[int]]):
	with open("foundids.txt", "w", encoding='utf8') as f:
		for channel, ids in messages.items():
			if ids is None or len(ids) == 0:
				print(f'No messages found for channel: {channel} (skipping)')
				continue

			print(f'Saving channel: {channel}')
			f.write(f'{channel}\n')

def dump_dir(path: str, years: List[str]) -> List[int]:
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
			# discord timestamps: yyyy-mm-dd hh:mm:ss
			year = message["Timestamp"].split('-', 1)[0]
			if year not in years:
				continue

			messages.append(message['ID'])

	return messages

def dump_all(years: List[str]) -> Dict[str, List[int]]:
	messages = {}
	for channel in os.listdir('messages'):
		path = f'messages/{channel}'
		if not os.path.isdir(path):
			continue

		channel_id = channel.replace('c', '', 1)
		messages[channel_id] = dump_dir(path, years)

	return messages

def get_year_range() -> List[str]:
	years = input('Enter years to search messages with (separated by commas):\n> ')
	return list(set([year.strip() for year in years.split(',') if year.strip()]))

def main():
	years = get_year_range()
	messages = dump_all(years)
	save_channels(messages)

if __name__ == "__main__":
	main()
	print("Dumped to foundids.txt!")