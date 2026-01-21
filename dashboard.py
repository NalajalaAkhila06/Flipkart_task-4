"""
Operations Dashboard
"""

class Dashboard:
    def __init__(self, config):
        self.config = config
        
    def display_dashboard(self, **kwargs):
        """Display operations dashboard"""
        flight_logs = kwargs.get('flight_logs', {})
        delays = kwargs.get('delays', [])
        crew = kwargs.get('crew', {})
        loads = kwargs.get('loads', {})
        health_alerts = kwargs.get('health_alerts', {})
        route_alerts = kwargs.get('route_alerts', {})
        
        print("\n" + "="*60)
        print(" AIRLINE OPERATIONS DASHBOARD")
        print("="*60)
        
        print(f"\nFlights Monitored: {len(flight_logs.get('engine', []))}")
        print(f"Predicted Delays: {len(delays)}")
        print(f"Health Alerts: {len(health_alerts.get('engine_alerts', []))}")
        print(f"Route Alerts: {len(route_alerts.get('route_alerts', []))}")
        
        if delays:
            print("\n DELAY PREDICTIONS:")
            for delay in delays:
                print(f"  Flight {delay.get('flight_id')}: {delay.get('predicted_delay_minutes')} min")
        
        print("\n" + "="*30)
