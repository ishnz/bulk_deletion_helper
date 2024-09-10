# Behavior of scripts:
## dumpallmessages.py
This script searches through your messages folder and dumps every single channel ID it will find in the package.

It's saved into `messages.txt`
## dumpmessagesbyyear.py
This script searches for channel ID's and logs them in `foundids.txt` where you sent your last message in a specified at the beginning by the user year.
## dumpchannelids.py
This script asks for a text file full of channel ID's (more in How To Use section) and it will dump them from the package.
## blacklistdumpchannelids.py
This script asks for a text file full of channel ID's (more in How To Use section) and will dump everything but the channels you have provided.
# How to use:
## dumpallmessages.py & dumpmessagesbyyear.py
Place it in your package directory and run
## dumpchannelids.py & duplicatechecker.py & blacklistdumpchannelids.py
Have a .txt full of existing channel ids in your package/messages directory in this format:

```
1234567890123456
1234567890123456
1234567890123456
1234567890123456
```

Place the file in your package directory and run (optional for duplicatechecker.py)

Specify the .txt filename while execution and make sure it's in the same path as the script.
