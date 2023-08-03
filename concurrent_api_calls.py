import requests
import concurrent.futures

# Set the API endpoint URL
API_URL = "http://localhost:8090/"

# Set the number of concurrent requests you want to simulate
CONCURRENT_REQUESTS = 10000

# Set the total number of requests to be made
TOTAL_REQUESTS = 10000

# Function to make the API call
def make_api_call(url):
    response = requests.get(url)
    return response.status_code

# Execute the API calls concurrently
with concurrent.futures.ThreadPoolExecutor(max_workers=CONCURRENT_REQUESTS) as executor:
    urls = [API_URL] * TOTAL_REQUESTS
    results = list(executor.map(make_api_call, urls))

# Count the successful and failed requests
successful_requests = results.count(200)
failed_requests = TOTAL_REQUESTS - successful_requests

print(f"Successful Requests: {successful_requests}")
print(f"Failed Requests: {failed_requests}")
