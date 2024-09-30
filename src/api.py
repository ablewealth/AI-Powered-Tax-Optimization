from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
import logging
import os
from model import TaxOptimizerModel  # Make sure to import your model class

class TaxOptimizerAPI:
    def __init__(self):
        self.app = Flask(__name__)
        CORS(self.app)
        self.model = self.load_model()
        self.setup_logging()

        # Define routes
        self.app.add_url_rule('/optimize_tax', 'optimize_tax', self.optimize_tax, methods=['POST'])

    def setup_logging(self):
        log_folder = 'log'
        os.makedirs(log_folder, exist_ok=True)
        logging.basicConfig(filename=os.path.join(log_folder, 'api.log'),
                            level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s')
        self.logger = logging.getLogger()

    def load_model(self):
        try:
            model_instance = TaxOptimizerModel()  # Ensure you initialize your model class
            return model_instance.load_model()
        except Exception as e:
            self.logger.error(f'Error loading model: {e}')
            raise

    def optimize_tax(self):
        try:
            data = request.json
            input_features = np.array(data['features']).reshape(1, -1)

            prediction = self.model.predict(input_features)
            self.logger.info(f'Prediction made: {prediction[0]}')
            return jsonify({'optimized_tax': prediction[0]})
        except Exception as e:
            self.logger.error(f'Error during tax optimization: {e}')
            return jsonify({'error': 'An error occurred during prediction.'}), 500

    def run(self):
        self.app.run(debug=True)

if __name__ == "__main__":
    api = TaxOptimizerAPI()
    api.run()
