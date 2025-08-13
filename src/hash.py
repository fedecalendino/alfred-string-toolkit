import hashlib

from classes import Action


class HashAction(Action):
    def __init__(self, method: callable):
        super().__init__(method.__name__.replace("openssl_", ""))
        self.method = method

    def __call__(self, string: str) -> str:
        string = string.encode()
        digest = self.method(string)
        return digest.hexdigest()


name = "hash"

actions = [
    HashAction(hashlib.sha3_512),
    HashAction(hashlib.sha512),
    HashAction(hashlib.sha3_384),
    HashAction(hashlib.sha384),
    HashAction(hashlib.sha3_256),
    HashAction(hashlib.sha256),
    HashAction(hashlib.sha3_224),
    HashAction(hashlib.sha224),
    HashAction(hashlib.md5),
]
