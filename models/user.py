import binascii
import hashlib
import os


class User:

    __username: str
    __password: str

    @staticmethod
    def hash_password(password):
        """Hash a password for storing."""
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
        pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),
                                      salt, 100000)
        pwdhash = binascii.hexlify(pwdhash)
        return (salt + pwdhash).decode('ascii')

    @staticmethod
    def verify_password(stored_password, provided_password):
        """Verify a stored password against one provided by user"""
        salt = stored_password[:64]
        stored_password = stored_password[64:]
        pwdhash = hashlib.pbkdf2_hmac('sha512',
                                      provided_password.encode('utf-8'),
                                      salt.encode('ascii'),
                                      100000)
        pwdhash = binascii.hexlify(pwdhash).decode('ascii')
        return pwdhash == stored_password


def init(self, username: str, password: str):
    self.__username = username
    self.__password = password


def get_username(self):
    return self.__username


def get_password(self):
    return self.__password


def set_username(self, new_username):
    self.__username = new_username


def set_password(self, new_password):
    self.__password = new_password


def __str__(self) -> str:

    res = f"username: {self.__username} \n"
    res += f"password: {self.__password} "
    return res
