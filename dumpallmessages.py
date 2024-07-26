import json
import os

def change_to_package_dir():
    os.chdir("messages")

def dump_channel_from_cur_dir(output_file):
    print("Dumping channel from " + os.getcwd())
    with open("channel.json", 'r') as f:
        channel = json.load(f)
        id = channel["id"]
        chn_id = str(id) + ":\n"
    with open("messages.json", encoding='utf-8', errors='ignore') as f:
        messages = json.load(f)
        if (messages == []):
            os.chdir("..")
            return
        content = chn_id
        for message in messages:
            content = content + str(message["ID"]) +", "
        content = content[:-2] + "\n\n"
        output_file.write(content)
    os.chdir("..")

def dump_all():
    output_file = open("messages.txt", "w")
    change_to_package_dir()
    subdirs = [x[0] for x in os.walk(os.getcwd())]
    for subdir in subdirs:
        if subdir == os.getcwd():
            continue
        os.chdir(subdir)
        dump_channel_from_cur_dir(output_file)
    

def main():
    dump_all()

if __name__ == "__main__":
    main()
    print("Dumped to messages.txt!")