import requests

#Try GET for all
resp = requests.get('http://localhost:5050/api/v1/advs/').json()
print(resp)

#Try POST
resp = requests.post('http://localhost:5050/api/v1/advs/',
                          json={"author": "Test",
                                "title": "test",
                                "description": "test"})
print(resp)


# Try GET by id
resp = requests.get('http://localhost:5050/api/v1/adv/1').json()
print(resp)

#Try PUT by id
response = requests.put('http://localhost:5050/api/v1/adv/1', json={"title": "sometitle", "description": "somedescription"})
print(response)

#Try DELETE by id
response = requests.delete('http://localhost:5050/api/v1/adv/3')
print(response)