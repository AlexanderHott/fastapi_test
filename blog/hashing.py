from passlib.context import CryptContext


class Hash:
    __password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    @staticmethod
    def bcrypt(password: str):
        return Hash.__password_context.hash(password)
