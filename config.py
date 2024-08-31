"""
General Settings
API_ID, API_HASH: You can get these from https://my.telegram.org
DELETE_COMMAND: True if you want the selfbot to delete all commands before replying
                False if you want the selfbot to edit the command to the response text

LOG_COMMAND_USAGE: True if you want all command uses to be saved to the .log files and the console
LOG_DELETED_MESSAGES: True if you want all deleted messages in PMs and MM groups to be logged to .log and console

You must restart the selfbot if you are making and config changes
"""
API_ID = 123
API_HASH = ""
PREFIX = "."

DELETE_COMMAND = True


"""
Addresses Module
You only need to add the address to the crypto you are using.
"""
ADDRESSES = {
    "btc": "bc1.....",
    "eth": "0x......",
    "sol": "",
    "ltc": "",
    "xmr": "",
    "trx": "",
    "ton": ""
}

"""
AFK Module
"""
AFK_REASON = "I am currently offline and will message you when I return."

"""
Middleman Module
SECONDARY_ACCOUNT: This allows you to run the selfbot on an alt account, and run the commands on your main
CONTROLLED_BY_ID: This is your user ID (only to be used when you're running with an alt account)
MIDDLEMAN_GROUP:
    - name: The name of the group chat
    - bio: The bio of the group chat
    - photo: The group chat profile picture, this must be the file name and the file should be in the same folder as main.py
    - start_text: The text the bot will send in the group when it's made
FEE: Your Middleman fee as a %, IE if your fee is 5%, put 5
MINIMUM_FEE: Your minimum MM fee
"""
SECONDARY_ACCOUNT = False
CONTROLLED_BY_ID = None
MIDDLEMAN_GROUP = {
    "name": "Middleman GC",
    "bio": "Middleman GC bio",
    "photo": None,
    "start_text": "Hello, thanks for using me as your middleman. Please state the deal"
}
FEE = 5
MINIMUM_FEE = 10
TOS = "I am not responsible for anything at all.. ever."

"""
Highlight Module
"""
HIGHLIGHT_WORDS = [
    "word1",
    "word2",
]