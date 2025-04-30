def calculate_wpm(typed_text, duration_seconds):
    words = len(typed_text.strip().split())
    minutes = duration_seconds / 60
    if minutes == 0:
        return 0
    return round(words / minutes)
