"""
Passenger Load Predictor
"""

class LoadPredictor:
    def __init__(self, config):
        self.config = config
        
    def predict_loads(self, flight_logs):
        """Predicting passenger loads"""
        predictions = []
        
        for passenger_log in flight_logs.get('passenger', []):
            predictions.append({
                'flight_id': passenger_log.get('flight_id'),
                'predicted_load': passenger_log.get('booked'),
                'load_factor': (passenger_log.get('booked', 0) / passenger_log.get('capacity', 1)) * 100
            })
        
        return {
            'flight_predictions': predictions
        }
