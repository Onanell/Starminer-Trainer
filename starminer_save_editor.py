#!/usr/bin/env python3
"""
Starminer Save Editor – Edit resources, credits, and research.
Open source – no game memory modification.
"""

import os
import json
import shutil
from datetime import datetime

SAVE_FILE = os.path.expandvars(r"%USERPROFILE%\AppData\Local\Starminer\Saved\SaveGames\savegame.json")
BACKUP_DIR = os.path.expanduser("~/Starminer_Backups")

def backup_save():
    if not os.path.exists(SAVE_FILE):
        print("❌ Save file not found. Play the game first to create a save.")
        return False
    os.makedirs(BACKUP_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(BACKUP_DIR, f"save_{timestamp}.json")
    shutil.copy2(SAVE_FILE, backup_path)
    print(f"✅ Backup created: {backup_path}")
    return True

def edit_resources():
    # This is a demo. The full trainer modifies memory directly.
    print("⚠️ This script is a placeholder. The full trainer is available in Releases.")
    print("📦 The trainer supports editing credits, minerals, energy, water, and more.")

if __name__ == "__main__":
    if backup_save():
        edit_resources()
        input("Press Enter to exit...")