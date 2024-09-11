import json
import os

opening_text = """
Disclaimer: 
This will only return channel IDs from servers you are currently in.
This will not work for user or group DMs.

Please enter a text file with the server IDs you want to retrieve channel IDs from:
"""

exit_text = "Press Enter to exit..."

def format_ids(channel_ids):
    new = []
    for id in channel_ids:
        new.append("c" + id)
    return new

def get_server_channel_ids():
    print(opening_text)
    
    server_ids_file = input()

    try:
        with open(server_ids_file, 'r') as f:
            server_ids = f.read().splitlines()
        return server_ids
    except FileNotFoundError:
        print(f"Error: The file '{server_ids_file}' was not found.")
        input(exit_text)
        exit()

def dump_channel(output_file, server_ids):
    with open("channel.json", 'r') as f:
        channel = json.load(f)

        channel_id = channel.get("id", "")
        channel_name = channel.get("name", "")

        guild_id = channel.get("guild", {}).get("id", "")
        guild_name = channel.get("guild", {}).get("name", "")

    if guild_id == "":
        return

    if not guild_id in server_ids:
        return

    output_file.write(str(channel_id) + "\n")

    print(f"{channel_id} ({channel_name}) from {guild_id} ({guild_name}): \n")

    os.chdir("..")

def dump_all():
    server_ids = get_server_channel_ids()
    output_file = open("foundfromserver.txt", "w")
    
    os.chdir("messages")

    subdirs = [x[0] for x in os.walk(os.getcwd())]
    for subdir in subdirs:
        if subdir == os.getcwd():
            continue
        os.chdir(subdir)
        dump_channel(output_file, server_ids)  

    output_file.close()

def main():
    dump_all()
    print("Finished! Please confirm the above output of channel IDs is correct.")
    input(exit_text)

if __name__ == "__main__":
    main()

# python getserverschannelids.py
