 Movie Rating Prediction

## Project Overview
This project aims to develop a machine learning model to predict movie ratings based on various features such as genre, director, and actors. By analyzing historical movie data, the model explores how different factors influence movie ratings and provides insights into user and critic preferences.

## Objectives
- **Analyze** historical movie data to identify factors affecting movie ratings.
- **Build** a predictive regression model for movie ratings.
- **Demonstrate** the application of data preprocessing, feature engineering, and machine learning techniques.

## Dataset
The dataset contains information about movies, including:
- **Name**: Title of the movie.
- **Year**: Year of release.
- **Duration**: Runtime of the movie in minutes.
- **Genre**: Movie genre(s).
- **Rating**: User or critic rating (target variable).
- **Votes**: Number of votes the movie received.
- **Director**: Name of the director.
- **Actor 1, Actor 2, Actor 3**: Names of the top three actors.

### Key Statistics
- **Rows**: 15,509
- **Columns**: 10
- **Missing Data**: Various columns contain missing values, particularly `Duration`, `Rating`, and `Actor` columns.

## Approach

### 1. **Data Preprocessing**
- Handle missing values using imputation or removal.
- Convert categorical variables (e.g., `Genre`, `Director`) into numeric formats using encoding techniques.
- Standardize non-standard formats in columns such as `Year` and `Votes`.
- Normalize or scale features where necessary.

### 2. **Feature Engineering**
- Extract new features, such as the number of genres or leading actors.
- Use one-hot encoding or frequency encoding for categorical variables.

### 3. **Model Development**
- Experiment with multiple regression models, including:
  - Linear Regression
  - Random Forest Regressor
  - Gradient Boosting Regressor
- Use hyperparameter tuning to optimize model performance.

### 4. **Evaluation Metrics**
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R-squared (R²)

### 5. **Documentation and Visualization**
- Visualize feature importance and the relationship between predicted and actual ratings.

## Repository Structure
```
movie-rating-prediction/
│
├── data/
│   └── IMDb Movies India.csv
├── notebooks/
│   └── data_exploration.ipynb
├── src/
│   ├── data_preprocessing.py
│   ├── feature_engineering.py
│   └── model_training.py
├── README.md
├── requirements.txt
└── .gitignore
```

## Challenges Faced
- **Data Cleaning**: Handling missing and inconsistent data across multiple columns.
- **Feature Engineering**: Balancing the trade-off between simplicity and predictive power.
- **Model Optimization**: Fine-tuning hyperparameters for better accuracy without overfitting.


## Results
- Achieved [model performance metrics, e.g., RMSE: 1.23, R²: 0.87].
- Identified key factors influencing movie ratings, such as [genre and director importance].


## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/movie-rating-prediction.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Open the Jupyter Notebook:
   ```bash
   jupyter notebook notebooks/data_exploration.ipynb
   ```
4. Run the scripts in the `src/` directory to preprocess data and train the model.

## License
This project is licensed under the [MIT License](LICENSE).

