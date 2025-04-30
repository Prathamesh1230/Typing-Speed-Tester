class TestResult:
    def __init__(self, wpm, accuracy, duration):
        self.wpm = wpm
        self.accuracy = accuracy
        self.duration = duration

    def display(self):
        print("\n--- Test Results ---")
        print(f"Typing Speed: {self.wpm} WPM")
        print(f"Accuracy: {self.accuracy}%")
        print(f"Time Taken: {round(self.duration, 2)} seconds")
