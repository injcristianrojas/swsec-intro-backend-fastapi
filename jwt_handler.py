from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from datetime import UTC, datetime, timedelta

import jwt

SECRET_KEY = "123"
ALGORITHM = "HS256"

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def create_access_token(username, user_type):
    payload = {
        "sub": username,
        "type": user_type,
        "exp": datetime.now(UTC) + timedelta(hours=6),
    }
    encoded_jwt = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_token(token, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload.get("sub")
    except jwt.InvalidTokenError:
        raise credentials_exception


def get_current_user(token=Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    return verify_token(token, credentials_exception)
