import os
import logging
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from data_preprocessing import DataPreprocessing  # Ensure you have the correct import

class TaxOptimizerModel:
    def __init__(self):
        self.model = None
        self.logger = self.setup_logging()
        self.data_loader = DataPreprocessing('D:/AI-Powered Tax Optimization/data/historical_data.csv', 'D:/AI-Powered Tax Optimization/data/tax_regulations.csv')

    def setup_logging(self):
        log_folder = 'log'
        os.makedirs(log_folder, exist_ok=True)
        logging.basicConfig(filename=os.path.join(log_folder, 'model_training.log'),
                            level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s')
        logger = logging.getLogger()
        return logger

    def train_model(self):
        try:
            historical_data, _ = self.data_loader.load_data()  # Use the instance method
            X_train, X_test, y_train, y_test = self.data_loader.preprocess_data(historical_data)
            
            self.model = RandomForestRegressor()
            self.model.fit(X_train, y_train)
            self.logger.info('Model training completed successfully.')

            predictions = self.model.predict(X_test)
            mse = mean_squared_error(y_test, predictions)
            self.logger.info(f'Model Mean Squared Error: {mse:.2f}')
            print(f'Model Mean Squared Error: {mse:.2f}')

            # Save the model
            self.save_model('D:/AI-Powered Tax Optimization/src/tax_optimizer_model.pkl')

        except Exception as e:
            self.logger.error(f'Error during model training: {e}')
            raise

    def save_model(self, model_filename):
        try:
            joblib.dump(self.model, model_filename)
            self.logger.info(f'Model saved successfully as {model_filename}.')
        except Exception as e:
            self.logger.error(f'Error saving model: {e}')
            raise

    def load_model(self):
        try:
            model = joblib.load('D:/AI-Powered Tax Optimization/src/tax_optimizer_model.pkl')
            self.logger.info('Model loaded successfully.')
            return model
        except Exception as e:
            self.logger.error(f'Error loading model: {e}')
            raise

if __name__ == "__main__":
    tax_optimizer = TaxOptimizerModel()
    tax_optimizer.train_model()
