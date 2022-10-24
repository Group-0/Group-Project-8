from ast import And
from flask import Flask, jsonify
import hashlib
import json
import sys
import random
import requests
import private

app = Flask(__name__)
url = "https://hooks.slack.com/services/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"

@app.route("/")
def hello_world():
  return "<p>Hello, World!</p>"

# Claire's code
# /md5/<string>

@app.route("/md5/<string>")
def md5(string):
  
  hash_obj = hashlib.md5(string.encode())
  hashstring = hash_obj.hexdigest()
  success = {
    "input": string,
    "output": hashstring
  }
  return json.dumps(success)

# Roxanna's code
# /factorial/<int>
@app.route("/factorial/<int:num>")
def factorial(num):
  original_num = num
  fact = 1

  not_factorial = {
    "input": original_num , 
    "output": "ERROR, Integer must be a positive integer"
  }

  if num < 0:
    return json.dumps(not_factorial)
  else:
    while(num > 1):
      fact *= num
      num-= 1
      
  factorial = {
    "input": original_num, 
    "output": fact
  }
  
  return json.dumps(factorial)

# Juan's code
# /fibonacci/<int>
@app.route("/fibonacci/<int:size>")
def fibonacci_sequence(size):
  a = 0
  b = 1
  array = [0]
      # Check is n is less
      # than 0
  if size < 0:
    response = {
      "input": size,
      "output": "Error: Invalid input"
    }
    return response
          
      # Check is n is equal
      # to 0
  elif size == 0:
    response = {
      "input": size,
      "output": [0]
    }
    return response
  else:
    while b <= size:
      array.append(b)
      c = a + b
      a = b
      b = c
      
    response = {
      "input": size,
      "output": array
    }
    return response

# Irish's code
# /is-prime/<int>
@app.route("/is-prime/<int:num>")
def is_prime(num):
  prime = {
    "input": num, 
    "output": True
    }

  not_prime = {
    "input": num, 
    "output": False
    }

  if (num > 1):
    for counter in range(2, num):
      if (num % counter) == 0:
        return json.dumps(not_prime)
  elif num == 1:
    return json.dumps(not_prime)
  else:
    return jsonify({
      "input": num, 
      "output": "Error. Invalid input."
    })
  return json.dumps(prime)


# Paula's code
@app.route("/slack-alert/<string:message>")
def slack_alert(message):
  success = {
    "input": message,
    "output": True
  }
  
  fail = {
    "input": message,
    "output": False
  }
  
  url = private.url
  title = (f"New Incoming Message :zap:")
  slack_data = {
    "username": "ReveilleBot-Group0",
    "icon_url": "https://upload.wikimedia.org/wikipedia/commons/f/ff/Reveille-TAMU-Mascot.JPG",
    "attachments": [
      {
        "color": "#500000",
        "fields": [
          {
            "title": title,
            "value": message,
            "short": "false",
          }
        ]
      }
    ]
  }
  byte_length = str(sys.getsizeof(slack_data))
  headers = {'Content-Type': "application/json", 'Content-Length': byte_length}
  response = requests.post(url, data=json.dumps(slack_data), headers=headers)
  success_status = response.status_code == 200
  if not success_status:
    return json.dumps(fail)
  return json.dumps(success)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=4000)
