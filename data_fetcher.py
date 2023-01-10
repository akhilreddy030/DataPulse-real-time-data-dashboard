import requests

def get_data():
    response = requests.get('https://api.example.com/data')
    return response.json()  # Or process the data as needed
