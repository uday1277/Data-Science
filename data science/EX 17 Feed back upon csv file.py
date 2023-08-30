import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
import matplotlib.pyplot as plt

# Download stopwords if not already downloaded
nltk.download('stopwords')
nltk.download('punkt')

# Load the dataset from CSV
data = pd.read_csv('data.csv')

# Combine all feedback into a single string
all_feedback = ' '.join(data['feedback'])

# Tokenize and preprocess the text data
tokens = word_tokenize(all_feedback)
tokens = [token.lower() for token in tokens if token.isalpha()]
filtered_words = [word for word in tokens if word not in stopwords.words('english')]

# Calculate word frequencies
word_freq = Counter(filtered_words)

# Get user input for the number of top words to display
n = int(input("Enter the number of top words to display: "))

# Display the top N most frequent words and their frequencies
top_words = word_freq.most_common(n)
print(f"Top {n} most frequent words:")
for word, freq in top_words:
    print(f"{word}: {freq}")

# Create a bar graph to visualize the top N most frequent words and their frequencies
plt.bar([word for word, freq in top_words], [freq for word, freq in top_words])
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.title(f'Top {n} Most Frequent Words')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
