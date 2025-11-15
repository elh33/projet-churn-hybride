# main.py

import pandas as pd
from data.preprocessing import clean_data
from data.text_processing import process_text
from features.feature_engineering import create_features
from models.churn_model import ChurnModel
from models.text_model import TextModel
from models.hybrid_model import HybridModel
from evaluation.metrics import evaluate_model

def main():
    # Load data
    structured_data = pd.read_csv('data/structured_data.csv')
    text_data = pd.read_csv('data/text_data.csv')

    # Preprocess data
    cleaned_data = clean_data(structured_data)
    processed_text = process_text(text_data)

    # Feature engineering
    features = create_features(cleaned_data, processed_text)

    # Initialize models
    churn_model = ChurnModel()
    text_model = TextModel()
    hybrid_model = HybridModel(churn_model, text_model)

    # Train models
    hybrid_model.train(features)

    # Evaluate model
    results = evaluate_model(hybrid_model, features)
    print(results)

if __name__ == "__main__":
    main()