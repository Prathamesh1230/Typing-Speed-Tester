import tkinter as tk
import random
from logic import TypingLogic
from sentences import sentences

class TypingSpeedGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Tester")
        self.root.geometry("700x400")
        self.logic = None

        self.sentence = random.choice(sentences)

        self.label = tk.Label(root, text="Type this sentence:", font=("Arial", 16))
        self.label.pack(pady=10)

        self.target_display = tk.Label(root, text=self.sentence, font=("Courier", 14), wraplength=650)
        self.target_display.pack(pady=10)

        self.text_entry = tk.Text(root, height=5, font=("Courier", 14), wrap="word")
        self.text_entry.pack(pady=10)
        self.text_entry.bind("<FocusIn>", self.start_typing)

        self.result_label = tk.Label(root, text="", font=("Arial", 14))
        self.result_label.pack(pady=10)

        self.check_btn = tk.Button(root, text="Check Result", font=("Arial", 14), command=self.show_result)
        self.check_btn.pack(pady=5)

        self.reset_btn = tk.Button(root, text="Try Again", font=("Arial", 12), command=self.reset)
        self.reset_btn.pack(pady=5)

    def start_typing(self, event):
        if not self.logic:
            self.logic = TypingLogic(self.sentence)
            self.logic.start_timer()

    def show_result(self):
        typed_text = self.text_entry.get("1.0", tk.END).strip()
        if self.logic:
            self.logic.end_timer()
            wpm = self.logic.calculate_wpm(typed_text)
            accuracy = self.logic.calculate_accuracy(typed_text)
            self.result_label.config(text=f"WPM: {wpm}   Accuracy: {accuracy}%")

    def reset(self):
        self.sentence = random.choice(sentences)
        self.target_display.config(text=self.sentence)
        self.text_entry.delete("1.0", tk.END)
        self.result_label.config(text="")
        self.logic = TypingLogic(self.sentence)
