import os
import json

years = []
print("Enter years to search messages with (separated by commas): ")
years = input().split(",")
print("Searching for messages in years: " + str(years))

file = open("foundids.txt", "w")
os.chdir("messages")
subdirs = [x[0] for x in os.walk(os.getcwd())]
for subdir in subdirs:
    if subdir == os.getcwd():
        continue
    os.chdir(subdir)
    messages = json.load(open("messages.json", encoding='utf-8', errors='ignore'))
    if messages == []:
        os.chdir("..")
        continue
    year = messages[0]["Timestamp"]
    year = year[:4]
    if year not in years:
        os.chdir("..")
        continue
    with open("channel.json", 'r') as f:
            channel = json.load(f)
            id = channel["id"]
            print("Found channel " + str(id) + " Last message was in " + year)
            print("Content: " + messages[0]["Contents"])
            file.write(str(id) + "\n")
    os.chdir("..")


