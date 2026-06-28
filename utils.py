import json
import os


def load_history(file_path):
    if os.path.exists(file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                return json.load(file)
        except:
            return []

    return []


def save_history(file_path, history):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(history, file, indent=4, ensure_ascii=False)


def add_history(file_path, original, translated):
    history = load_history(file_path)

    history.append({
        "original": original,
        "translated": translated
    })

    save_history(file_path, history)