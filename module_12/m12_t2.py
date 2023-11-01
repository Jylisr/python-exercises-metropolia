#Module 12, task 2

import requests
import json

keyword = input("Enter the municipality: ")
request = "https://openweathermap.org/api"

try:
    response = requests.get(request).json()
    print(response)
except:
    print("Error")