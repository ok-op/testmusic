import os
from os import getenv
from dotenv import load_dotenv
from os import environ

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5827766615").split()))
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002126211125"))





#Port
PORT = os.environ.get("PORT", "8080")
