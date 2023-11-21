#Module 13, task 1
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/prime_number')
def prime_number():
    args = request.args
    num = int(args.get("num"))
    prime_num = False

    if num <= 1:
        result = {"num": num, "is_prime": False, "message": "Not a prime number"}
    else:
        for i in range(2, num):
            if (num % i) == 0:
                prime_num = True
                break

        if not prime_num:
            result = {"num": num, "is_prime": True, "message": f"{num} is a prime number"}
        else:
            result = {"num": num, "is_prime": False, "message": f"{num} is not a prime number"}

    return jsonify(result)

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)

