import yaml
import requests
import time
from collections import defaultdict

# Function to read YAML configuration
def read_config(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

# Function to check the health of endpoints
def check_health(endpoints):
    results = {}
    for endpoint in endpoints:
        url = endpoint['url']
        method = endpoint.get('method', 'GET')
        headers = endpoint.get('headers', {})
        body = endpoint.get('body', None)

        try:
            start_time = time.time()
            response = requests.request(method, url, headers=headers, data=body, timeout=5)
            latency = (time.time() - start_time) * 1000
            if 200 <= response.status_code < 300 and latency < 500:
                results[url] = 'UP'
            else:
                results[url] = 'DOWN'
        except requests.RequestException:
            results[url] = 'DOWN'

    return results

# Function to calculate availability percentage
def calculate_availability(health_log):
    availability = {}
    for domain, statuses in health_log.items():
        up_count = statuses.count('UP')
        availability[domain] = round(100 * up_count / len(statuses))
    return availability

# Main execution
if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print("Usage: python main.py <config_file_path>")
        sys.exit(1)

    config_path = sys.argv[1]
    endpoints = read_config(config_path)

    health_log = defaultdict(list)

    try:
        while True:
            health_results = check_health(endpoints)
            for endpoint in endpoints:
                url = endpoint['url']
                domain = url.split('/')[2]
                health_log[domain].append(health_results[url])

            availability = calculate_availability(health_log)
            for domain, percent in availability.items():
                print(f"{domain} has {percent}% availability percentage")

            time.sleep(15)
    except KeyboardInterrupt:
        print("Program terminated.")
