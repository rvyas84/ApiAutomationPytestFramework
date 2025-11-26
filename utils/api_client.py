import requests
import random
import string

class APIClient:
    BASE_URL = "https://gorest.co.in/public/v2"

    def __init__(self):
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer 4d10ef7527d6f8e3f5a961df8d074dc2df34d6de7f36edff5efb026b65ec26c6"
        }
    
    def get(self, endpoint):
        url = f"{self.BASE_URL}/{endpoint}"
        print(url)
        response = requests.get(url, headers = self.headers)
        return response
    
    def post(self, payload, endpoint):
        url = f"{self.BASE_URL}/{endpoint}"
        print(url)
        response = requests.post(url, json=payload, headers = self.headers)
        return response
    
    def put(self, payload, endpoint):
        url = f"{self.BASE_URL}/{endpoint}"
        print(url)
        response = requests.put(url, json=payload, headers = self.headers)
        return response
    
    def delete(self, endpoint):
        url = f"{self.BASE_URL}/{endpoint}"
        print(url)
        response = requests.delete(url, headers = self.headers)
        return response
    
    def generate_random_string(self):
        string_length = 10
        random_string = ''.join(random.choice(string.ascii_lowercase) for _ in range(string_length))
        return random_string