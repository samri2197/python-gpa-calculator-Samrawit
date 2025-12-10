import json
import os

def load(path, default):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    
    if not os.path.exists(path):
        save(path, default)
        return default
    
    try:
        with open(path, 'r') as f:
            return json.load(f)
    except:
        return default

def save(path, data):
    try:
        with open(path, 'w') as f:
            json.dump(data, f, indent=2)
        return True
    except Exception as e:
        print(f"Error saving: {e}")
        return False
