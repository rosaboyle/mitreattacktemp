
import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
    text = re.sub(r'\W', ' ', text)  # Remove special characters
    text = text.lower()  # Convert to lowercase
    words = text.split()
    # words = [word for word in words if word not in stop_words]
    return ' '.join(words)

preprocessed_texts = [preprocess_text(text) for text in texts]

# print(preprocessed_texts)

# from transformers import pipeline

# # Load pre-trained model and tokenizer
# model_name = "gpt-4"
# nlp = pipeline("text-generation", model=model_name)

# def analyze_text(text):
#     result = nlp(text, max_length=500)
#     return result[0]['generated_text']

# profiles = [analyze_text(text) for text in preprocessed_texts]