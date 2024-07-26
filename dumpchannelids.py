import json
import os

def change_to_package_dir():
    os.chdir("messages")

def format_ids(channel_ids):
    new = []
    for id in channel_ids:
        new.append("c" + id)
    return new

def get_channel_ids():
    print("Enter the text file containing the channel IDs.")
    channel_ids_file = input()
    with open(channel_ids_file, 'r') as f:
        channel_ids = f.read().splitlines()
    channel_ids = format_ids(channel_ids)
    return channel_ids

def dump_channel(id, output_file):
    print("Dumping channel " + id + "...")
    os.chdir(id)
    output_file.write(id.replace("c", "") + ":\n")
    with open("messages.json", encoding='utf-8', errors='ignore') as f:
        messages = json.load(f)
        content = ""
        for message in messages:
            content = content + str(message["ID"]) +", "
        content = content[:-2] + "\n\n"
        output_file.write(content)
    os.chdir("..")

def dump_all(ids):
    output_file = open("messages.txt", "w")
    change_to_package_dir()
    for id in ids:
        dump_channel(id, output_file)

def main():
    ids = get_channel_ids()
    dump_all(ids)

if __name__ == "__main__":
    main()
    print("Dumped to messages.txt!")