import json
a='{"id":12,"name":"satish","age":"25","place":"vizag"}';
x=json.loads(a)
y=json.dumps(x)
print(y["name"])
