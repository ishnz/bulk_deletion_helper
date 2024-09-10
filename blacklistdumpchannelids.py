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
    print("Enter the text file containing the channel IDs to exclude.")
    exclude_ids_file = input()
    with open(exclude_ids_file, 'r') as f:
        exclude_ids = f.read().splitlines()
    exclude_ids = format_ids(exclude_ids)
    return exclude_ids

def get_all_channel_dirs():
    
    return [d for d in os.listdir() if os.path.isdir(d)]

def dump_channel(id, output_file):
    print("Dumping channel " + id + "...")
    os.chdir(id)
    output_file.write(id.replace("c", "") + ":\n")
    with open("messages.json", encoding='utf-8', errors='ignore') as f:
        messages = json.load(f)
        content = ""
        for message in messages:
            content = content + str(message["ID"]) + ", "
        content = content[:-2] + "\n\n"
        output_file.write(content)
    os.chdir("..")

def dump_all(exclude_ids):
    output_file = open("messages.txt", "w")
    change_to_package_dir()

    all_channel_dirs = get_all_channel_dirs()

    channels_to_dump = [id for id in all_channel_dirs if id not in exclude_ids]

    for id in channels_to_dump:
        dump_channel(id, output_file)

def main():
    exclude_ids = get_channel_ids()
    dump_all(exclude_ids)

if __name__ == "__main__":
    main()
    print("Dumped to messages.txt!")
