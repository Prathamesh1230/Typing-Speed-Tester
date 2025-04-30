import json
import os

class HistoryStorage:
    def __init__(self):
        self.filename = "typing_history.json"

    def save_result(self, result):
        data = self.load_results()
        data.append({
            "wpm": result.wpm,
            "accuracy": result.accuracy,
            "duration": result.duration
        })
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=4)

    def load_results(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, "r") as f:
            return json.load(f)
