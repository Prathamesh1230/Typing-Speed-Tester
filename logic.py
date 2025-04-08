import time

class TypingLogic:
    def __init__(self, sentence):
        self.target = sentence
        self.start_time = None
        self.end_time = None

    def start_timer(self):
        self.start_time = time.time()

    def end_timer(self):
        self.end_time = time.time()

    def calculate_wpm(self, typed_text):
        if self.start_time and self.end_time:
            words = len(typed_text.strip().split())
            minutes = (self.end_time - self.start_time) / 60
            return round(words / minutes) if minutes > 0 else 0
        return 0

    def calculate_accuracy(self, typed_text):
        correct = 0
        for i, char in enumerate(typed_text):
            if i < len(self.target) and char == self.target[i]:
                correct += 1
        return round((correct / len(self.target)) * 100, 2)
