# AMKUSH USERBOT CONFIGURATION
import os

# Bot Configuration
BOT_TOKEN = "8075698787:AAE1LbpVJXwvX4R1TxO5zyb7oJk19MiKbnk"
OWNER_ID = 7577966487
BOT_NAME = "ªmkush"

# MongoDB Configuration
MONGO_URL = "mongodb+srv://amkush.bvmzl26.mongodb.net/"
MONGO_USERNAME = "yourplaypass22"
MONGO_PASSWORD = ""  # Add password if needed
MONGO_DB_NAME = "amkush_userbot"

# API Keys
GIPHY_API_KEY = "K7IhPIj8d63xTyNI8JSoYEWoelXYMztw"

# Command Prefixes
COMMAND_PREFIXES = [".", "/", "$"]

# Auto-delete timers (seconds)
COMMAND_DELETE_TIMER = 5
PROGRESS_DELETE_TIMER = 10
RULES_DELETE_TIMER = 15

# Rate limiting
PAIR_RATE_LIMIT = 3  # requests per hour
MAX_WARNINGS = 3

# File paths
SESSION_DIR = "sessions/"
TEMP_DIR = "temp/"
DOWNLOADS_DIR = "downloads/"

# Ensure directories exist
os.makedirs(SESSION_DIR, exist_ok=True)
os.makedirs(TEMP_DIR, exist_ok=True)
os.makedirs(DOWNLOADS_DIR, exist_ok=True)

# Bot settings
AUTO_DELETE_COMMANDS = True
BOLD_MESSAGES = True
USE_EMOJIS = True

# Feature toggles
ENABLE_GIPHY_GIFS = True
ENABLE_AI_FEATURES = True
ENABLE_MEDIA_DOWNLOAD = True
ENABLE_STICKER_TOOLS = True

# Default settings for new users
DEFAULT_USER_SETTINGS = {
    "welcome_enabled": False,
    "antilink_enabled": False,
    "antilink_action": "mute",
    "typing_style": False,
    "ghost_mode": False,
    "auto_react": False,
    "auto_read": False,
    "require_api": False,
    "rate_limit_pair": True,
    "mode": "private"
}

# UI Styling
BOLD_CHARS = {
    'a': '𝐚', 'b': '𝐛', 'c': '𝐜', 'd': '𝐝', 'e': '𝐞', 'f': '𝐟', 'g': '𝐠', 'h': '𝐡',
    'i': '𝐢', 'j': '𝐣', 'k': '𝐤', 'l': '𝐥', 'm': '𝐦', 'n': '𝐧', 'o': '𝐨', 'p': '𝐩',
    'q': '𝐪', 'r': '𝐫', 's': '𝐬', 't': '𝐭', 'u': '𝐮', 'v': '𝐯', 'w': '𝐰', 'x': '𝐱',
    'y': '𝐲', 'z': '𝐳', 'A': '𝐀', 'B': '𝐁', 'C': '𝐂', 'D': '𝐃', 'E': '𝐄', 'F': '𝐅',
    'G': '𝐆', 'H': '𝐇', 'I': '𝐈', 'J': '𝐉', 'K': '𝐊', 'L': '𝐋', 'M': '𝐌', 'N': '𝐍',
    'O': '𝐎', 'P': '𝐏', 'Q': '𝐐', 'R': '𝐑', 'S': '𝐒', 'T': '𝐓', 'U': '𝐔', 'V': '𝐕',
    'W': '𝐖', 'X': '𝐗', 'Y': '𝐘', 'Z': '𝐙', '0': '𝟎', '1': '𝟏', '2': '𝟐', '3': '𝟑',
    '4': '𝟒', '5': '𝟓', '6': '𝟔', '7': '𝟕', '8': '𝟖', '9': '𝟗'
}

def make_bold(text):
    """Convert text to bold Unicode characters"""
    if not BOLD_MESSAGES:
        return text
    return ''.join(BOLD_CHARS.get(char, char) for char in text)

# Logging configuration
import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('amkush_bot.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)