import time
from test_logic import TypingTest
from utils import clear_screen, countdown, get_random_paragraph

class TypingTesterUI:
    def __init__(self):
        self.test = TypingTest()

    def run(self):
        while True:
            clear_screen()
            print("===== Typing Speed Tester =====")
            print("1. Start Test")
            print("2. View History")
            print("3. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.start_test()
            elif choice == '2':
                self.test.view_history()
                input("Press Enter to continue...")
            elif choice == '3':
                print("Thank you for using Typing Speed Tester!")
                break
            else:
                print("Invalid choice. Try again.")

    def start_test(self):
        paragraph = get_random_paragraph()
        print("\nGet ready to type the following text:\n")
        print(f"\"{paragraph}\"\n")
        countdown()
        input("Press Enter to start typing...")

        start_time = time.time()
        typed_text = input("\nStart typing:\n")
        end_time = time.time()

        duration = end_time - start_time
        self.test.evaluate(paragraph, typed_text, duration)
 