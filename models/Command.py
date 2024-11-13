from dataclasses import dataclass


@dataclass
class Command:
    """
    Structure basic commands used by the app.
    """
    alias: list[str]  # alternative keywords
    description: str
    keyword: str  # primary keyword
    usage: str  # usage syntax, if any
    enabled: bool = True
    reply: bool = False
    restricted: bool = False

# Define commands
commands = {
    "ping": Command(alias=[], description="Check if the bot is online.", keyword="ping", usage="ping"),
    "flip": Command(alias=["fl1p"], description="Flip a table.", keyword="flip", usage="flip", ),
    "hello": Command(alias=["hello", "hi"], description="Universal greeting.", keyword="hello", usage="hello", reply=True),
    "pin": Command(alias=["save"], description="Pin (save) a message.", keyword="pin", usage="pin <message>", reply=True),
    "unpin": Command(alias=["unsave"], description="Unpin (unsave) a message.", keyword="unpin", usage="unpin <message>", reply=True),
    "remind": Command(alias=["reminder", "remindme"], description="Set a reminder.", keyword="remind", usage="remind <time> <message>", reply=True),
    "forget": Command(alias=[], description="Forget a stored reminder.", keyword="forget", usage="forget <reminder_id>", reply=True),
    "forecast": Command(alias=["weather"], description="Post weather forecast.", keyword="forecast", usage="forecast", enabled=False),
    "users": Command(alias=["members"], description="Get list of users.", keyword="users", usage="users", restricted=True),
    "kick": Command(alias=["boot"], description="Show user to door.", keyword="kick", usage="kick <uid>", restricted=True, reply=True),
    "ban": Command(alias=[], description="Apply hammer.", keyword="ban", usage="ban <uid>", restricted=True, reply=True),
    "unban": Command(alias=[], description="De-apply hammer.", keyword="unban", usage="unban <uid>", restricted=True, reply=True),
}

# Example of accessing commands
for cmd_name, cmd in commands.items():
    print(f"Command: {cmd_name}")
    print(f"Description: {cmd.description}")
    print(f"Usage: {cmd.usage}")
    print("-" * 20)
