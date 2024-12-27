import pandas as pd
import numpy as np

def load_and_preprocess_data(file_path):
    # Load the dataset
    data = pd.read_csv(file_path, encoding='ISO-8859-1')
    
    # Handle missing values (you can choose to drop or fill them)
    data = data.dropna(subset=['Rating', 'Genre', 'Year', 'Duration', 'Director'])
    
    # Convert 'Duration' to numeric values (removing ' min' and converting to float)
    data['Duration'] = data['Duration'].str.replace(' min', '').astype(float)
    
    # Extract year from 'Year' column if needed (you can choose different strategies)
    data['Year'] = data['Year'].str.extract('(\d{4})').astype(float)
    
    return data



