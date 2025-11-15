def normalize_text(text):
    import re
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'\d+', '', text)  # Remove numbers
    text = re.sub(r'\s+', ' ', text).strip()  # Remove extra whitespace
    return text

def lemmatize_text(text):
    from nltk.stem import WordNetLemmatizer
    from nltk.tokenize import word_tokenize
    lemmatizer = WordNetLemmatizer()
    tokens = word_tokenize(text)
    lemmatized_text = ' '.join([lemmatizer.lemmatize(token) for token in tokens])
    return lemmatized_text

def remove_stopwords(text):
    from nltk.corpus import stopwords
    stop_words = set(stopwords.words('english'))
    tokens = text.split()
    filtered_text = ' '.join([word for word in tokens if word not in stop_words])
    return filtered_text

def process_text(text):
    text = normalize_text(text)
    text = lemmatize_text(text)
    text = remove_stopwords(text)
    return text