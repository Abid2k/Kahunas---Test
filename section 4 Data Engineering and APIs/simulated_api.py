import json
import random
from http.server import BaseHTTPRequestHandler, HTTPServer
from datetime import datetime

class FitnessDataAPIHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/fitness-data":
            
            fitness_data = {
                "timestamp": datetime.now().isoformat(),
                "steps": random.randint(1000, 15000),  
                "heart_rate": random.randint(60, 120) 
            }
            
            
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            
            
            self.wfile.write(json.dumps(fitness_data).encode("utf-8"))
        else:
            
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Endpoint not found.")

if __name__ == "__main__":
    host = "localhost"
    port = 8000
    server = HTTPServer((host, port), FitnessDataAPIHandler)
    print(f"Simulated API is running at http://{host}:{port}/fitness-data")
    server.serve_forever()
