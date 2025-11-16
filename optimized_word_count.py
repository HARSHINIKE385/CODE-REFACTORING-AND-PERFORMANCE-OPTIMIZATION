# optimized_word_count.py
from collections import Counter
import re
from typing import Dict

def word_count(file_path: str) -> Dict[str, int]:
    """Count frequency of words in a file, ignoring punctuation and case."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {file_path}")

    # Use regex to split words and remove punctuation
    words = re.findall(r'\b\w+\b', text.lower())
    
    return dict(Counter(words))

if __name__ == "__main__":
    import time
    start = time.time()
    print(word_count('sample.txt'))
    end = time.time()
    print(f"Time taken: {end-start:.4f} seconds")
