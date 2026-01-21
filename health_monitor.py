"""
Aircraft Health Monitor
"""

class HealthMonitor:
    def __init__(self, config):
        self.config = config
        
    def monitor_health(self, flight_logs):
        """Monitor aircraft health"""
        alerts = []
        
        for engine_log in flight_logs.get('engine', []):
            vibration = engine_log.get('metrics', {}).get('vibration', 0)
            
            if vibration > 8.0:
                alerts.append({
                    'flight_id': engine_log.get('flight_id'),
                    'severity': 'HIGH',
                    'message': f'High engine vibration: {vibration}'
                })
        
        return {
            'engine_alerts': alerts,
            'critical_alerts': []
        }
