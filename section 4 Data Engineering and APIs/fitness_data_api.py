import http.client
import json
import csv
import time

HOST = "localhost"
PORT = 8000
ENDPOINT = "/fitness-data"
CSV_FILE = "fitness_data.csv"

def fetch_fitness_data():
    
    conn = http.client.HTTPConnection(HOST, PORT)
    try:
        
        conn.request("GET", ENDPOINT)
        response = conn.getresponse()

        if response.status == 200:
            
            data = json.loads(response.read().decode("utf-8"))
            return data
        else:
            print(f"Failed to fetch data. HTTP Status: {response.status}")
            return None
    finally:
        conn.close()

def save_to_csv(data):
    
    try:
        with open(CSV_FILE, "r") as file:
            pass
        file_exists = True
    except FileNotFoundError:
        file_exists = False

    
    with open(CSV_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        
        
        if not file_exists:
            writer.writerow(["timestamp", "steps", "heart_rate"])
        
       
        writer.writerow([data["timestamp"], data["steps"], data["heart_rate"]])

if __name__ == "__main__":
    print("Starting data fetch...")
    for _ in range(10):  
        fitness_data = fetch_fitness_data()
        if fitness_data:
            print(f"Fetched data: {fitness_data}")
            save_to_csv(fitness_data)
        time.sleep(2)  
    print(f"Data saved to {CSV_FILE}")
