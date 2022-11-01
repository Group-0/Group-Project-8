from flask import jsonify
import requests
import json

# count of failed tests
count = 0

# md5 test code
r = requests.get("http://localhost:4000/md5/1")
j = r.json()
if (r.status_code == 200):
    print("✅")
else:
    print("❌")
    count += 1

r = requests.get("http://localhost:4000/md5/helloworld")
j = r.json()
if (r.status_code == 200):
    print("✅")
else:
    print("❌")
    count += 1

r = requests.get("http://localhost:4000/md5/test")
j = r.json()
if (r.status_code == 200):
    print("✅")
else:
    print("❌")
    count += 1

r = requests.get("http://localhost:4000/md5/912")
j = r.json()
if (r.status_code == 200):
    print("✅")
else:
    print("❌")
    count += 1

r = requests.get("http://localhost:4000/md5/hello")
j = r.json()
if (r.status_code == 200):
    print("✅")
else:
    print("❌")
    count += 1

# is-prime test code
r = requests.get("http://localhost:4000/is-prime/1")
j = r.json()
if (r.status_code == 200) and (j['output'] == False):
    print("✅")
else:
    print("❌ for is-prime/1. Expected Output: false")
    count += 1

r = requests.get("http://localhost:4000/is-prime/2")
j = r.json()
if (r.status_code == 200) and (j['output'] == True):
    print("✅")
else:
    print("❌ for is-prime/2. Expected Output: true")
    count += 1

r = requests.get("http://localhost:4000/is-prime/12345")
j = r.json()
if (r.status_code == 200) and (j['output'] == False):
    print("✅")
else:
    print("❌ for is-prime/12345. Expected Output: false")
    count += 1

r = requests.get("http://localhost:4000/is-prime/hello")
if (r.status_code == 404):
    print("✅")
else:
    print("❌ for is-prime/hello. Expected Status Code: 404")
    count += 1

r = requests.get("http://localhost:4000/is-prime/-1")
if (r.status_code == 404):
    print("✅")
else:
    print("❌ for is-prime/-1. Expected Status Code: 404")
    count += 1

r = requests.get("http://localhost:4000/is-prime/23.5")
if (r.status_code == 404):
    print("✅")
else:
    print("❌ for is-prime/23.5. Expected Status Code: 404")
    count += 1

# Factorial Test Code 
r = requests.get("http://localhost:4000/factorial/25")
j = r.json() 
if((r.status_code == 200) and j['output'] == 15511210043330985984000000):
    print("✅")
else: 
    print("❌")
    count += 1

r = requests.get("http://localhost:4000/factorial/85")
j = r.json()
if((r.status_code == 200) and j['output'] == 281710411438055027694947944226061159480056634330574206405101912752560026159795933451040286452340924018275123200000000000000000000):
    print("✅")
else: 
    print("❌")
    count += 1

r = requests.get("http://localhost:4000/factorial/33")
j = r.json()
if((r.status_code == 200) and j['output'] == 8683317618811886495518194401280000000):
    print("✅")
else: 
    print("❌")
    count += 1

r = requests.get("http://localhost:4000/factorial/-5")
if (r.status_code == 404):
    print("✅")
else:
    print("❌ for factorial -5, Expected Status Code: 404")
    count += 1

# Fibonacci test code
r = requests.get("http://localhost:4000/fibonacci/1000")
j = r.json()
if (r.status_code == 200) and (j['output'] == [0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987]):
    print("✅")
else:
    print("❌")

r = requests.get("http://localhost:4000/fibonacci/8")
j = r.json()
if (r.status_code == 200) and (j['output'] == [0,1,1,2,3,5,8]):
    print("✅")
else:
    print("❌")

r = requests.get("http://localhost:4000/fibonacci/0")
j = r.json()
if (r.status_code == 200) and (j['output'] == [0]):
    print("✅")
else:
    print("❌")

r = requests.get("http://localhost:4000/fibonacci/1")
j = r.json()
if (r.status_code == 200) and (j['output'] == [0,1,1]):
    print("✅")
else:
    print("❌")

# Slack Alert test code
r = requests.get("http://localhost:4000/slack-alert/1")
j = r.json()
print("Testing slack-alert/1", end="\t\t\t\t")
if (r.status_code == 200) and (j['output'] == True):
    print("✅")
else:
    print("❌")
    count += 1

r = requests.get("http://localhost:4000/slack-alert/this%20is%20a%20test!")
j = r.json()
print("Testing slack-alert/this%20is%20a%20test!", end="\t")
if (r.status_code == 200) and (j['output'] == True):
    print("✅")
else:
    print("❌")
    count += 1

r = requests.get("http://localhost:4000/slack-alert/this\nis\na\n\ntest")
j = r.json()
print("Testing slack-alert/this\\nis\\na\\n\\ntest", end="\t\t")
if (r.status_code == 200) and (j['output'] == True):
    print("✅")
else:
    print("❌")
    count += 1

r = requests.get("http://localhost:4000/slack-alert/reveillebot")
j = r.json()
print("Testing slack-alert/reveillebot", end="\t\t\t")
if (r.status_code == 200) and (j['output'] == True):
    print("✅")
else:
    print("❌")
    count += 1

r = requests.get("http://localhost:4000/slack-alert/howdy%20world!")
j = r.json()
print("Testing slack-alert/howdy%20world!", end="\t\t")
if (r.status_code == 200) and (j['output'] == True):
    print("✅")
else:
    print("❌")
    count += 1



# ---------------------------- Project 8 Test Code --------------------------- #

# url = "http://localhost:4000/keyval"
# response = requests.post(url, json={"key": "testing", "value": "newval"})
# print(response)

# url = "http://localhost:4000/keyval"
# response = requests.post(url, json={"key": "testing", "value": "123"})
# print(response)

print(count)
if count == 0:
    print("Keeping it 💯% successful.")
else:
    print(count, " test cases did not pass.")


#Roxanna's Test for new /keyval/ endpoint POST and GET
#(post)
url = "http://localhost:4000/keyval"
response = requests.post(url, json={"key": "testing", "value": "newval"})
if (response.status_code == 200):
    print("New Key Value Created")
else:
    print("ERROR! Test case did not pass")
    count += 1 

url = "http://localhost:4000/keyval"
response = requests.post(url, json={"key": "testing", "value": "125"})
if (response.status_code >= 409):
    print("Unable to add pair: Key already exists")
else: 
    print("ERROR! Test case did not pass")
    count += 1 

#(GET)
url = "http://localhost:4000/keyval/testing"
response = requests.get(url)
if (response.status_code >= 200 ):
    print("Key Value was succesfully retrieved ")
else:
    print("ERROR! Test case did not pass")
    count += 1 

url = "http://localhost:4000/keyval/92"
response = requests.get(url)
if (response.status_code == 200):
    print("Unable to retrieve pair: Invalid request")
else: 
    print("ERROR! Test case did not pass")
    count += 1 

url = "http://localhost:4000/keyval/program"
response = requests.get(url)
if (response.status_code == 200):
    print("Unable to retrieve pair: Key does not exist")
else: 
    print("ERROR! Test case did not pass")
    count += 1 
