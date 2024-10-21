import requests
import json

result = requests.get("https://jsonplaceholder.typicode.com/todos")

# result = result.text    #It is json string information.
# print(type(result)) #str
# print(result)

#
result = json.loads(result.text) #converts the json str information to python list object.
print(type(result)) #list

for i in result:
    print(i)

# for i in result:
#     if i["userId"] == 1:
#         print(i)
#         print(i["title"])
