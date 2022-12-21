
import jwt



JWT_SECRET = "this_is_just_for_testing"



def create_jwt(payload):
    token = jwt.encode(
        payload,
        JWT_SECRET,
        algorithm="HS256"
    )
    return token


def validate_jwt(token): 
    try:
        payload = jwt.decode(token, JWT_SECRET, "HS256")
    except:
        raise

    return payload
    
