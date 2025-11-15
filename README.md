# projet-churn-hybride

## Overview
The "projet-churn-hybride" is a customer churn prediction application that integrates both structured data analysis and text analysis. The project aims to predict customer churn by leveraging various data sources, including tabular data and textual data from customer interactions.

## Directory Structure
The project is organized into the following directories:

- **src/**: Contains the main source code for data processing, model training, and evaluation.
  - **data/**: Scripts for data preprocessing and text processing.
  - **models/**: Implementation of different models for churn prediction.
  - **features/**: Functions for feature engineering and text feature extraction.
  - **evaluation/**: Metrics for evaluating model performance.
  - **main.py**: The main entry point for the application.

- **notebooks/**: Jupyter notebooks for exploratory data analysis and model training.
  
- **tests/**: Unit tests for ensuring the functionality of data processing and model classes.

- **config/**: Configuration file for project settings.

- **requirements.txt**: Lists the required Python packages for the project.

## Installation
To set up the project, clone the repository and install the required dependencies:

```bash
git clone <repository-url>
cd projet-churn-hybride
pip install -r requirements.txt
```

## Usage
1. **Data Processing**: Use the scripts in the `src/data/` directory to preprocess your data.
2. **Feature Engineering**: Utilize the functions in `src/features/` to create new features.
3. **Model Training**: Train your models using the Jupyter notebooks in the `notebooks/` directory.
4. **Evaluation**: Evaluate your models with the metrics provided in `src/evaluation/metrics.py`.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.