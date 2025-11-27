import requests
import random
import string
import os
from dotenv import load_dotenv

load_dotenv() 

class APIClient:
    BASE_URL = "https://gorest.co.in/public/v2"

    def __init__(self):
        token = os.getenv("API_TOKEN")

        if not token:
            raise ValueError("⚠ GOREST_API_TOKEN environment variable not set")

        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
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