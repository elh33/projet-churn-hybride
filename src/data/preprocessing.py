def handle_missing_values(df):
    # Fill missing values with the mean for numerical columns
    for column in df.select_dtypes(include=['float64', 'int64']).columns:
        df[column].fillna(df[column].mean(), inplace=True)
    
    # Fill missing values with the mode for categorical columns
    for column in df.select_dtypes(include=['object']).columns:
        df[column].fillna(df[column].mode()[0], inplace=True)
    
    return df

def encode_categorical_variables(df):
    # Convert categorical variables to dummy/indicator variables
    df = pd.get_dummies(df, drop_first=True)
    return df

def preprocess_data(df):
    df = handle_missing_values(df)
    df = encode_categorical_variables(df)
    return df