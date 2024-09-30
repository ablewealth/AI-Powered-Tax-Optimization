import pandas as pd
import logging
import os
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline


class DataPreprocessing:
    def __init__(self, historical_data_path, regulations_path):
        self.historical_data_path = historical_data_path
        self.regulations_path = regulations_path
        self.model = None
        self.logger = self.setup_logging()

    def setup_logging(self):
        log_folder = 'log'
        os.makedirs(log_folder, exist_ok=True)
        logging.basicConfig(filename=os.path.join(log_folder, 'data_preprocessing.log'), 
                            level=logging.INFO, 
                            format='%(asctime)s - %(levelname)s - %(message)s')
        logger = logging.getLogger()
        return logger

    def load_data(self):
        try:
            historical_data = pd.read_csv(self.historical_data_path)
            regulations = pd.read_csv(self.regulations_path)
            self.logger.info('Data loaded successfully.')
            return historical_data, regulations
        except Exception as e:
            self.logger.error(f'Error loading data: {e}')
            raise

    def preprocess_data(self, historical_data):
        try:
            # Fill missing values
            historical_data.fillna(0, inplace=True)
            
            # Separate features and target
            X = historical_data.drop('target', axis=1)
            y = historical_data['target']
            
            # Identify categorical and numerical columns
            categorical_cols = X.select_dtypes(include=['object']).columns.tolist()
            numerical_cols = X.select_dtypes(exclude=['object']).columns.tolist()
            
            # Create a preprocessing pipeline
            preprocessor = ColumnTransformer(
                transformers=[
                    ('num', 'passthrough', numerical_cols),  # Keep numerical columns as is
                    ('cat', OneHotEncoder(), categorical_cols)  # One-hot encode categorical columns
                ]
            )
            
            # Transform the features
            X_transformed = preprocessor.fit_transform(X)
            
            # Split the data
            X_train, X_test, y_train, y_test = train_test_split(X_transformed, y, test_size=0.2, random_state=42)
            
            self.logger.info('Data preprocessed successfully.')
            return X_train, X_test, y_train, y_test
        except Exception as e:
            self.logger.error(f'Error during preprocessing: {e}')
            raise

    def train_model(self, X_train, y_train):
        try:
            self.model = RandomForestRegressor()  # Example regression model
            self.model.fit(X_train, y_train)
            self.logger.info('Model trained successfully.')
        except Exception as e:
            self.logger.error(f'Error training model: {e}')
            raise

    def evaluate_model(self, X_test, y_test):
        try:
            predictions = self.model.predict(X_test)
            
            # Calculate regression metrics
            mae = mean_absolute_error(y_test, predictions)
            mse = mean_squared_error(y_test, predictions)
            r2 = r2_score(y_test, predictions)
            
            self.logger.info(f'Model evaluation completed. MAE: {mae:.2f}, MSE: {mse:.2f}, R²: {r2:.2f}')
            
            return mae, mse, r2
        except Exception as e:
            self.logger.error(f'Error evaluating model: {e}')
            raise

    def save_model(self, model_filename):
        try:
            with open(model_filename, 'wb') as model_file:
                pickle.dump(self.model, model_file)
            self.logger.info(f'Model saved successfully as {model_filename}.')
        except Exception as e:
            self.logger.error(f'Error saving model: {e}')
            raise

if __name__ == '__main__':
    dp = DataPreprocessing('D:/AI-Powered Tax Optimization/data/historical_data.csv', 'D:/AI-Powered Tax Optimization/data/tax_regulations.csv')
    
    historical_data, regulations = dp.load_data()
    X_train, X_test, y_train, y_test = dp.preprocess_data(historical_data)
    dp.train_model(X_train, y_train)
    dp.evaluate_model(X_test, y_test)
    dp.save_model('D:/AI-Powered Tax Optimization/src/model.pkl')
