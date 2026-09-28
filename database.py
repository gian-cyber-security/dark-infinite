"""
DARK INFINITE - Database Layer
SQLite for sessions, users, custom bugs, attack logs
"""

import sqlite3
import time
from config import DATABASE_PATH

def init_db():
    """Initialize database with all tables"""
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    
    # Users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            is_active INTEGER DEFAULT 1,
            created_at REAL DEFAULT 0
        )
    ''')
    
    # Custom bugs table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS custom_bugs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL,
            payload TEXT NOT NULL,
            created_by TEXT DEFAULT 'admin',
            created_at REAL DEFAULT 0
        )
    ''')
    
    # Attack logs
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS attack_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            target TEXT NOT NULL,
            bug_type TEXT NOT NULL,
            sender_mode TEXT DEFAULT 'global',
            sender_number TEXT,
            payload_count INTEGER DEFAULT 0,
            status TEXT DEFAULT 'pending',
            timestamp REAL DEFAULT 0
        )
    ''')
    
    # Private senders
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS private_senders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            number TEXT UNIQUE NOT NULL,
            added_by TEXT DEFAULT 'admin',
            is_active INTEGER DEFAULT 1,
            created_at REAL DEFAULT 0
        )
    ''')
    
    # Chat messages
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS chat_messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            message TEXT NOT NULL,
            timestamp REAL DEFAULT 0
        )
    ''')
    
    conn.commit()
    conn.close()
    print("[DB] Database initialized at", DATABASE_PATH)

def get_db():
    """Get database connection"""
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def add_user(username, password):
    conn = get_db()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO users (username, password, created_at) VALUES (?, ?, ?)",
            (username, password, time.time())
        )
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def verify_user(username, password):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=? AND is_active=1",
        (username, password)
    )
    user = cursor.fetchone()
    conn.close()
    return user is not None

def save_custom_bug(name, payload):
    conn = get_db()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO custom_bugs (name, payload, created_at) VALUES (?, ?, ?)",
            (name, payload, time.time())
        )
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def get_custom_bugs():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM custom_bugs")
    bugs = cursor.fetchall()
    conn.close()
    return bugs

def log_attack(target, bug_type, sender_mode, sender_number, payload_count, status):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        """INSERT INTO attack_logs 
        (target, bug_type, sender_mode, sender_number, payload_count, status, timestamp)
        VALUES (?, ?, ?, ?, ?, ?, ?)""",
        (target, bug_type, sender_mode, sender_number, payload_count, status, time.time())
    )
    conn.commit()
    conn.close()

def save_chat_message(username, message):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO chat_messages (username, message, timestamp) VALUES (?, ?, ?)",
        (username, message, time.time())
    )
    conn.commit()
    conn.close()

def get_chat_messages(limit=50):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM chat_messages ORDER BY timestamp DESC LIMIT ?",
        (limit,)
    )
    messages = cursor.fetchall()
    conn.close()
    return messages

def add_private_sender(number):
    conn = get_db()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO private_senders (number, created_at) VALUES (?, ?)",
            (number, time.time())
        )
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def get_private_senders():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM private_senders WHERE is_active=1")
    senders = cursor.fetchall()
    conn.close()
    return senders

def get_attack_history(limit=100):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM attack_logs ORDER BY timestamp DESC LIMIT ?",
        (limit,)
    )
    logs = cursor.fetchall()
    conn.close()
    return logs