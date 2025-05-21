import jwt
import datetime
from settings import setting

def generate_jwt_token(user_id, expiration_days=7):
    payload = {
        "user_id": user_id,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(days=expiration_days),
        "iat": datetime.datetime.utcnow()
    }
    token = jwt.encode(payload, setting.SECRET_KEY, algorithm="HS256")
    return token

def decode_jwt_token(token):
    try:
        payload = jwt.decode(token, setting.SECRET_KEY, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None