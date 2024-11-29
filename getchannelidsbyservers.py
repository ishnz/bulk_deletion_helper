import json
import os
from typing import List

def save_channels(channels: List[str]):
	with open("channels.txt", "w", encoding='utf8') as f:
		for channel in channels:
			print(f'Saving channel: {channel}')
			f.write(f'{channel}\n')

def dump_all(server_ids: List[str]) -> List[str]:
	channels = []
	for channel in os.listdir('messages'):
		path = f'messages/{channel}'
		if not os.path.isdir(path):
			continue

		with open(f'{path}/channel.json', 'r', encoding='utf8') as f:
			channel_obj = json.load(f)

			channel_id = channel_obj.get('id', '')
			channel_name = channel_obj.get('name', '')
			guild_id = channel_obj.get('guild', {}).get('id', '')
			guild_name = channel_obj.get('guild', {}).get('name', '')

		if not guild_id:
			continue

		if guild_id not in server_ids:
			continue

		print(f'Found channel: {channel_id} (#{channel_name}) from {guild_id} ("{guild_name}")')
		channels.append(channel_id)

	return channels

def get_server_ids():
	while True:
		file = input("Enter the text file containing the server IDs to fetch channels for:\n> ")
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
	server_ids = get_server_ids()
	channels = dump_all(server_ids)
	save_channels(channels)

if __name__ == "__main__":
	main()
	print("Dumped to channels.txt!")