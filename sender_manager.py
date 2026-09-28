"""
DARK INFINITE - Sender Manager
Manages global and private sender rotation
"""

import random
import threading
from config import GLOBAL_SENDERS
from db.database import get_private_senders, add_private_sender

class SenderManager:
    """Manages sender number rotation and routing"""
    
    def __init__(self):
        self.global_senders = GLOBAL_SENDERS
        self.lock = threading.Lock()
        self.rotation_index = 0
    
    def get_global_sender(self):
        """Get a global sender (round-robin rotation)"""
        with self.lock:
            sender = self.global_senders[self.rotation_index % len(self.global_senders)]
            self.rotation_index += 1
            return sender
    
    def get_random_global(self):
        """Get a random global sender"""
        return random.choice(self.global_senders)
    
    def get_private_senders(self):
        """Get all active private senders from DB"""
        senders = get_private_senders()
        return [s['number'] for s in senders] if senders else []
    
    def add_private(self, number):
        """Add a private sender number"""
        return add_private_sender(number)
    
    def get_sender(self, mode='global'):
        """Get sender based on mode"""
        if mode == 'global':
            return self.get_global_sender()
        elif mode == 'private':
            privates = self.get_private_senders()
            if not privates:
                return None
            return random.choice(privates)
        else:
            return self.get_global_sender()
    
    def get_all_global(self):
        """Return all global senders"""
        return self.global_senders
    
    def get_stats(self):
        """Get sender statistics"""
        return {
            "global_count": len(self.global_senders),
            "global_numbers": self.global_senders,
            "private_count": len(self.get_private_senders()),
            "private_numbers": self.get_private_senders(),
            "current_rotation_index": self.rotation_index
        }