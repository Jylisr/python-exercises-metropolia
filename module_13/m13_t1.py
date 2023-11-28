#Module 13, task 1
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/prime_number/<num>')
def prime_number(num):
    num = int(num)
    if num > 1:
        for i in range(2, int(num / 2) + 1):
            if num % i == 0:
                prime = f"{num} is not a prime number"
                break
            else:
                prime = f"{num} is a prime number"
    else:
        prime = f"{num} is a prime number"
    response = {
        "prime" : prime,
        "status" : 200
    }
    return response




if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)

