def create_interaction_features(data):
    # Example function to create interaction features
    data['interaction_feature'] = data['feature1'] * data['feature2']
    return data

def create_aggregated_features(data):
    # Example function to create aggregated statistics
    aggregated = data.groupby('category').agg({'value': ['mean', 'sum', 'count']})
    aggregated.columns = ['mean_value', 'sum_value', 'count_value']
    return aggregated.reset_index()

def create_features(data):
    # Combine all feature engineering functions
    data = create_interaction_features(data)
    aggregated_features = create_aggregated_features(data)
    return data, aggregated_features