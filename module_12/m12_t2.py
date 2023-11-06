#Module 12, task 2

import requests
import json

keyword = input("Enter the municipality: ")
request = "https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}"

try:
    response = requests.get(request).json()
    print(response)
except:
    print("Error")

#Can't call, requires subscription