TITLE = """=== Smart Contacts ===\n"""

RECORDED = "contact(s) recorded.\n"


ASK_CMD = "\nType commands here (\"h\" for help): "


INFO_CMD = """List of available commands:


    - a         create new contact
    - d         delete contact
    - h         display this help
    - i "name"  display contact info
    - m "name"  modify contact info\n
"""


CMDS = {
    "a": "add",
    "d": "delete",
    "h": "diplay_help",
    "i": "diplay_info",
    "m": "modify_info"


}


PATH = "./backup/save.json"

INFOS_REQUEST = {
    "name": "Enter name: ",
    "lastname" : "Enter lastname: ",
    "phone" : "Enter phone number: ",
    "email": "Enter an email: "
}

