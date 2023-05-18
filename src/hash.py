import hashlib


def hash(string: str, method: callable) -> str:
    string = string.encode()
    digest = method(string)
    return digest.hexdigest()


def sha3_512(string: bytes) -> str:
    return hash(string, hashlib.sha3_512)


def sha_512(string: bytes) -> str:
    return hash(string, hashlib.sha512)


def sha3_384(string: bytes) -> str:
    return hash(string, hashlib.sha3_384)


def sha_384(string: bytes) -> str:
    return hash(string, hashlib.sha384)


def sha3_256(string: bytes) -> str:
    return hash(string, hashlib.sha3_256)


def sha_256(string: bytes) -> str:
    return hash(string, hashlib.sha256)


def sha3_224(string: bytes) -> str:
    return hash(string, hashlib.sha3_224)


def sha_224(string: bytes) -> str:
    return hash(string, hashlib.sha224)


def md5(string: bytes) -> str:
    return hash(string, hashlib.md5)


name = "hash"

actions = {
    "SHA3-512": sha3_512,
    "SHA-512": sha_512,
    "SHA3-384": sha3_384,
    "SHA-384": sha_384,
    "SHA3-256": sha3_256,
    "SHA-256": sha_256,
    "SHA3-224": sha3_224,
    "SHA-224": sha_224,
    "MD5": md5,
}
