import os
from pathlib import Path

class Config:
    
    API_ID = "22136772"
    API_HASH = "7541e5b6d298eb1f60dac89aae92868c"
    BOT_TOKEN = "7587525827:AAEDwwPfawc0WyTHMMxLknP45Fic3qKQrh8"
    SESSION_NAME = "ScreenshotGenRobot
    LOG_CHANNEL = "-1002638440257"
    DATABASE_URL = "mongodb+srv://storymachineofficial:storymachineofficial@cluster0.snchtpl.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    AUTH_USERS = [8083702486]
    MAX_PROCESSES_PER_USER = int(os.environ.get('MAX_PROCESSES_PER_USER', 5))
    MAX_TRIM_DURATION = int(os.environ.get('MAX_TRIM_DURATION', 10000))
    TRACK_CHANNEL = int(os.environ.get('TRACK_CHANNEL', True))
    SLOW_SPEED_DELAY = int(os.environ.get('SLOW_SPEED_DELAY', 5))
    HOST = os.environ.get('HOST', '')
    
    SCRST_OP_FLDR = Path('screenshots/')
    SMPL_OP_FLDR = Path('samples/')
    THUMB_OP_FLDR = Path('thumbnails/')
    COLORS = ['white', 'black', 'red', 'blue', 'green', 'yellow', 'orange', 'purple', 'brown', 'gold', 'silver', 'pink']
    FONT_SIZES_NAME = ['Small', 'Medium', 'Large']
    FONT_SIZES = [30, 40, 50]
