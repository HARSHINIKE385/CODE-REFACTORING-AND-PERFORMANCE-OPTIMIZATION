# old_word_count.py
def word_count(file_path):
    file = open(file_path, 'r')
    text = file.read()
    file.close()
    words = text.split(' ')
    count = {}
    for word in words:
        word = word.lower()
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count

if __name__ == "__main__":
    import time
    start = time.time()
    print(word_count('sample.txt'))
    end = time.time()
    print(f"Time taken: {end-start:.4f} seconds")
