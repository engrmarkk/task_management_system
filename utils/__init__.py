from flask_jwt_extended import create_access_token
from datetime import timedelta

def return_access_token(user):
    try:
        return create_access_token(
            identity=user, expires_delta=timedelta(days=1)
        )
    except Exception as e:
        print(e, "error@Return_access_token")
        return None
