from result import TestResult
from storage import HistoryStorage
from accuracy import calculate_accuracy
from wpm import calculate_wpm

class TypingTest:
    def __init__(self):
        self.storage = HistoryStorage()

    def evaluate(self, original, typed, duration):
        accuracy = calculate_accuracy(original, typed)
        wpm = calculate_wpm(typed, duration)

        result = TestResult(wpm=wpm, accuracy=accuracy, duration=duration)
        result.display()
        self.storage.save_result(result)

    def view_history(self):
        print("\n--- Test History ---")
        results = self.storage.load_results()
        if not results:
            print("No test history found.")
        for idx, res in enumerate(results, 1):
            print(f"{idx}. WPM: {res['wpm']}, Accuracy: {res['accuracy']}%, Time: {round(res['duration'], 2)}s")
