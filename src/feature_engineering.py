import pandas as pd

def generate_features(data):
    # Example of a new feature: log transform of Duration (if skewed)
    data['Log_Duration'] = data['Duration'].apply(lambda x: np.log(x) if x > 0 else 0)
    
    # Example of converting categorical data to numeric (encoding genres or directors)
    data = pd.get_dummies(data, columns=['Genre', 'Director'], drop_first=True)
    
    return data

