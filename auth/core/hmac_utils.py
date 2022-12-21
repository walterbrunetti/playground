


import base64
import hashlib
import hmac



def make_digest_sha256(secret_shared_key: str, msg: str):
    digest = hmac.new(key=secret_shared_key.encode(), msg=str(msg).encode(), digestmod=hashlib.sha256).digest()  # returns binary
    return base64.b64encode(digest).decode('utf-8')


def make_digest_sha256_hex(secret_shared_key: str, msg: str):
    """
    It returns message authentication code of data as hexadecimal digits.
    Use base64 to ship binary data across the internet.
    """
    digest = hmac.new(key=secret_shared_key.encode(), msg=str(msg).encode(), digestmod=hashlib.sha256).hexdigest()
    return base64.b64encode(digest.encode('utf-8')).decode('utf-8')


"""
>>> ts = int(time.time())
>>> msg = '{}|{}'.format('username', ts)


"""

