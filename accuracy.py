def calculate_accuracy(original, typed):
    original_words = original.strip().split()
    typed_words = typed.strip().split()
    correct = 0

    for o, t in zip(original_words, typed_words):
        if o == t:
            correct += 1

    if not original_words:
        return 0
    accuracy = (correct / len(original_words)) * 100
    return round(accuracy, 2)
