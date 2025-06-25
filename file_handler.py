import json

def save_data(data):
    try:
        with open("transactions.json", "w") as f:
            json.dump(data, f)
    except Exception as e:
        print(f"Error saving file: {e}")

def load_data():
    try:
        with open("transactions.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except Exception as e:
        print(f"Error loading file: {e}")
        return []
