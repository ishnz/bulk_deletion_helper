import json
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def change_to_package_dir():
    os.chdir("messages")

def format_ids(channel_ids):
    new = []
    for id in channel_ids:
        new.append("c" + id)
    return new

def check_ids(ids):
    change_to_package_dir()
    cls()
    existing = []
    not_existing = []
    for id in ids:
        if os.path.exists(id):
            existing.append(id)
            continue;
        else:
            not_existing.append(id)
    if not_existing is not []:
        print("The following channel IDs do not exist:")
        id_strings = ', '.join(not_existing)
        print(id_strings)
        print("Do you wish to continue and exclude those? (y/n)")
        response = input()
        if response == "n":
            exit()
        else:
            return existing            

def check_for_duplicates(ids):
    seen = set()
    result = []
    for id in ids:
        if id not in seen:
            seen.add(id)
            result.append(id)
        else:
            print("Duplicate channel ID found: " + id + " Removing...")
    return result
        

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
    ids = check_ids(ids)
    ids = check_for_duplicates(ids)
    for id in ids:
        dump_channel(id, output_file)

def main():
    ids = get_channel_ids()
    dump_all(ids)

if __name__ == "__main__":
    main()
    print("Dumped to messages.txt!")
