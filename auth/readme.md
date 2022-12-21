

# Auth playground
This app pretends to play with JWT and HMAC by implementing 2 endpoints:
   - login
   - validate token

The payload used to create the JWT contains an HMAC signature that will be validated later on.


### Running the app

Create and activate a virtual env.

```
pip install -r auth/requirements.txt
python auth_index.py

```

### Try it

1- Log-in:

`curl http://127.0.0.1:5000/login -u my_user_name:my_temp_password -X POST`

2- Validate token returned in step #1:

`curl -H 'Authorization: Bearer <token>' http://127.0.0.1:5000/validate_token -X POST`



### Try it with a Python shell
```
import requests
import base64

payload = {}

# Log-in
requests.post('http://127.0.0.1:5000/login', auth=('user', 'pass'), data=payload)
>>> eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Indh

# alternative
# b64Val = base64.b64encode("userid:password")
# requests.post(http://127.0.0.1:5000/login, headers={"Authorization": "Basic %s" % b64Val}, data=payload)


# Validate token
requests.post('http://127.0.0.1:5000/validate_token', headers={'Authorization': <token>})


```

### HTTP request Auth header
`Authorization: <type> <credentials>`


```
Authorization: Basic base64-encoded(username:password)
Authorizarion: Bearer <token>

```


### JWT
JSON Web Token is an open industry standard used to share information between two entities.
JWT is a protocol for generating signed tokens containing claims. Claims is any information that you can represent in JSON-like format.
The tokens are signed either using a private secret or a public/private key.

```
>>> import jwt
>>> token = jwt.encode({"some": "payload"}, SECRET, algorithm="HS256")
>>> payload = jwt.decode(token, SECRET, "HS256")

```


### HMAC
HMAC stands for Hash based Message Authentication Code.
The HMAC is an algorithm that generates a hash of the message using a cryptographic hash function and a secret cryptographic key.
It can be used to check data for integrity and authenticity.
The HMAC construction can use any secure hash function, and will output a hash at the end. A middleman attacker could not generate a valid HMAC without knowledge of the key. So when we send encrypted data, it is a good idea to send an HMAC along with it, so that if the message is changed, the HMAC will be invalid.





