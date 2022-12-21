
import datetime
import time
from typing import Dict

from flask import Flask, request
from core.jwt_utils import create_jwt, validate_jwt
from core.hmac_utils import make_digest_sha256, make_digest_sha256_hex


app = Flask(__name__)


@app.route('/login', methods=["POST"])
def login():
    auth = request.authorization
    username, psw = auth.username, auth.password
    
    # assume we vaidate credentials here
    
    payload = _generate_payload(username)
    token = create_jwt(payload)

    return token 


@app.route("/validate_token", methods=["POST"])
def validate_token():
    auth_header = request.headers.get("Authorization")
    token = auth_header.split(" ")[1]

    payload = validate_jwt(token)
    time_stamp = payload.get("ts")
    username = payload.get("username")
    message = f'{time_stamp}|{username}'
    
    signature = make_digest_sha256_hex(username, message)

    # validate signature
    assert signature == payload.get("signature")
    return "success!"



def _generate_payload(username: str) -> Dict[str, str]:
    time_stamp = int(time.time())
    message = f'{time_stamp}|{username}'

    payload = {
            "username": username,
            "expires": str(datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(days=1)),
            #"iat": str(datetime.datetime.utcnow()),
            "is_admin": True,
            "signature": make_digest_sha256_hex(username, message),
            "ts": time_stamp
    }

    return payload



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

