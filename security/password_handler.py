from passlib.context import CryptContext

PWD_CONTEXT = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password:str):
    """Create password hash
    """
    return PWD_CONTEXT.hash(password)


def verify_password(plain_password, password_hash):
    """Verify password against the password_hash
    """
    return PWD_CONTEXT.verify(plain_password, password_hash)