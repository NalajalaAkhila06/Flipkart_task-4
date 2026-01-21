"""
Predictive Flight Delay Engine
"""

class DelayPredictor:
    def __init__(self, config):
        self.config = config
        
    def predict_delays(self, flight_logs):
        """Predict delays for flights"""
        predictions = []
        
        # Checking the each flight
        for engine_log in flight_logs.get('engine', []):
            delay = 0
            reasons = []
            
            # Checking the engine thrust
            thrust = engine_log.get('metrics', {}).get('engine_thrust', 100)
            if thrust < 70:
                delay += 25
                reasons.append('Low engine thrust')
            
            # Checking the vibration
            vibration = engine_log.get('metrics', {}).get('vibration', 0)
            if vibration > 7.5:
                delay += 15
                reasons.append('High vibration')
            
            if delay > 0:
                predictions.append({
                    'flight_id': engine_log.get('flight_id'),
                    'predicted_delay_minutes': delay,
                    'reasons': reasons
                })
        
        return predictions  
