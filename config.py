import os
from os import getenv
from dotenv import load_dotenv

load_dotenv(".env")


API_ID = int(getenv("API_ID", "16209450")) #optional
API_HASH = getenv("API_HASH", "a4573c55ebf7c23038b927997447b78d") #optional
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1863087128").split()))
OWNER_ID = getenv("OWNER_ID")
MONGO_URL = getenv("MONGO_URL")
BOT_TOKEN = getenv("BOT_TOKEN", "")
ALIVE_PIC = getenv("ALIVE_PIC")
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER", "true")
OPENAI_API = getenv("OPENAI_API", "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", "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")
OPENAI_API_KEY = getenv("OPENAI_API_KEY", "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")
RMBG_API = getenv("RMBG_API", "3RCCWg8tMBfDWdAs44YMfJmC")
BOTLOG_CHATID = int(getenv("BOTLOG_CHATID") or 0)
PM_LIMIT = int(getenv("PM_LIMIT") or 5)
BLACKLIST_GCAST = {int(x) for x in getenv("BLACKLIST_GCAST", "").split()}
GIT_TOKEN = getenv("GIT_TOKEN", "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") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/dimasly/eYon-Ubot")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
BRANCH = getenv("BRANCH", "main") #don't change
CMD_HNDLR = getenv("CMD_HNDLR", ".")
STRING_SESSION1 = getenv("STRING_SESSION1", "")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
STRING_SESSION11 = getenv("STRING_SESSION11", "")
STRING_SESSION12 = getenv("STRING_SESSION12", "")
STRING_SESSION13 = getenv("STRING_SESSION13", "")
STRING_SESSION14 = getenv("STRING_SESSION14", "")
STRING_SESSION15 = getenv("STRING_SESSION15", "")



