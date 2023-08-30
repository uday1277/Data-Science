import string
from collections import defaultdict

def preprocess_text(text):
     
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text.lower()

def calculate_frequency(text):
    word_freq = defaultdict(int)  
    
    words = text.split()  
    
    for word in words:
        word_freq[word] += 1
    
    return word_freq

def main():
    file_path = "C:/Users/udayg/OneDrive/Desktop/data science/sample.txt"
    
    with open(file_path, 'r') as file:
        text = file.read()
    
    preprocessed_text = preprocess_text(text)
    word_freq = calculate_frequency(preprocessed_text)
    
    
    for word, freq in word_freq.items():
        print(f"{word}: {freq}")
    
    
    with open("frequency_distribution.txt", 'w') as output_file:
        for word, freq in word_freq.items():
            output_file.write(f"{word}: {freq}\n")

if __name__ == "__main__":
    main()
