"""
Daily Report Generator
"""

from datetime import datetime

class ReportGenerator:
    def __init__(self, config):
        self.config = config
        
    def generate_daily_report(self, **kwargs):
        """Generate daily operations report"""
        date = kwargs.get('date', datetime.now().strftime('%Y-%m-%d'))
        
        report_path = f"output/reports/aviation_report_{date}.txt"
        
        with open(report_path, 'w') as f:
            f.write(f"Daily Aviation Operations Report\n")
            f.write(f"Date: {date}\n")
            f.write("="*80 + "\n")
            
            # Writing the flight data
            flight_logs = kwargs.get('flight_logs', {})
            f.write(f"\nFlights Processed: {len(flight_logs.get('engine', []))}\n")
            
            # Writing the delays
            delays = kwargs.get('delays', [])
            f.write(f"\nPredicted Delays: {len(delays)}\n")
            for delay in delays:
                f.write(f"  - Flight {delay.get('flight_id')}: {delay.get('predicted_delay_minutes')} min\n")
        
        return report_path
