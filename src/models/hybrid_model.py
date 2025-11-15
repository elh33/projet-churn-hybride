class HybridModel:
    def __init__(self, churn_model, text_model):
        self.churn_model = churn_model
        self.text_model = text_model

    def fit(self, X_structured, X_text, y):
        self.churn_model.fit(X_structured, y)
        self.text_model.fit(X_text, y)

    def predict(self, X_structured, X_text):
        churn_predictions = self.churn_model.predict(X_structured)
        text_predictions = self.text_model.predict(X_text)
        combined_predictions = self.combine_predictions(churn_predictions, text_predictions)
        return combined_predictions

    def combine_predictions(self, churn_predictions, text_predictions):
        # Example of combining predictions, can be adjusted based on specific needs
        return (churn_predictions + text_predictions) / 2

    def evaluate(self, X_structured, X_text, y_true):
        predictions = self.predict(X_structured, X_text)
        # Assuming a method to evaluate predictions is defined elsewhere
        return evaluate_model(predictions, y_true)