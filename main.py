"""
AI-Driven Airline Operations & Predictive Flight Management System
Main Orchestrator Module
"""

import os
import json
from datetime import datetime, timedelta
from modules.log_processor import LogProcessor
from modules.delay_predictor import DelayPredictor
from modules.crew_optimizer import CrewOptimizer
from modules.load_predictor import LoadPredictor
from modules.health_monitor import HealthMonitor
from modules.route_monitor import RouteMonitor
from modules.dashboard import Dashboard
from modules.reporter import ReportGenerator

class AirlineOpsAutomation:
    def __init__(self):
        """Initialize the airline operations automation system"""
        self.load_config()
        self.setup_directories()
        self.initialize_modules()
        
    def load_config(self):
        """Load configuration from JSON file"""
        try:
            with open('airline_config.json', 'r') as f:
                self.config = json.load(f)
            print(" Configuration loaded successfully")
        except FileNotFoundError:
            print("Warning: Config file not found, using defaults")
            self.config = {}
    
    def setup_directories(self):
        """Create necessary directories if they don't exist"""
        directories = ['logs', 'data', 'output/reports', 'output/alerts']
        for directory in directories:
            os.makedirs(directory, exist_ok=True)
        print("Directory structure verified")
    
    def initialize_modules(self):
        """Initialize all system modules"""
        self.log_processor = LogProcessor(self.config)
        self.delay_predictor = DelayPredictor(self.config)
        self.crew_optimizer = CrewOptimizer(self.config)
        self.load_predictor = LoadPredictor(self.config)
        self.health_monitor = HealthMonitor(self.config)
        self.route_monitor = RouteMonitor(self.config)
        self.dashboard = Dashboard(self.config)
        self.reporter = ReportGenerator(self.config)
        
        print(" All modules initialized successfully")
    
    def process_flight_data(self, flight_date):
        """Process all flight data for a given date"""
        print(f"\n{'=' * 60}")
        print(f"PROCESSING FLIGHT DATA FOR: {flight_date}")
        print(f"{'=' * 60}")

        flight_logs = self.log_processor.process_all_logs()
        delay_predictions = self.delay_predictor.predict_delays(flight_logs)
        crew_schedule = self.crew_optimizer.optimize_schedule(
            flight_logs, delay_predictions
        )
        load_predictions = self.load_predictor.predict_loads(flight_logs)
        health_alerts = self.health_monitor.monitor_health(flight_logs)
        route_alerts = self.route_monitor.monitor_routes(flight_logs)

        self.dashboard.display_dashboard(
            flight_logs=flight_logs,
            delays=delay_predictions,
            crew=crew_schedule,
            loads=load_predictions,
            health_alerts=health_alerts,
            route_alerts=route_alerts
        )

        report_path = self.reporter.generate_daily_report(
            date=flight_date,
            flight_logs=flight_logs,
            delays=delay_predictions,
            crew_schedule=crew_schedule,
            load_predictions=load_predictions,
            health_alerts=health_alerts,
            route_alerts=route_alerts
        )

        print(f"\n Daily report generated: {report_path}")

        return {
            "flight_logs": flight_logs,
            "delay_predictions": delay_predictions,
            "crew_schedule": crew_schedule,
            "load_predictions": load_predictions,
            "health_alerts": health_alerts,
            "route_alerts": route_alerts
        }
    
    def run_simulation(self, days=7):
        """Run a multi-day simulation"""
        results = {}
        for i in range(days):
            sim_date = datetime.now() + timedelta(days=i)
            date_str = sim_date.strftime("%Y-%m-%d")
            results[date_str] = self.process_flight_data(date_str)
        
        return results

def main():
    """Main execution function"""
    print("\n" + "✈️" * 30)
    print("   AIRLINE OPS AUTOMATION SYSTEM")
    print("✈️" * 30)
    
    # Initialize the system
    airline_system = AirlineOpsAutomation()
    
    # Run for today
    today = datetime.now().strftime("%Y-%m-%d")
    results = airline_system.process_flight_data(today)
    
    print("\n" + "=" * 50)
    print("  SYSTEM EXECUTION COMPLETE")
    print("=" * 50)

if __name__ == "__main__":
    main()
