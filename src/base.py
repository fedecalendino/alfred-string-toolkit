import base64


def decode(string: str, method: callable, to_upper: bool = False) -> str:
    if to_upper:
        string = string.upper()

    digest = method(string)
    return digest.decode("utf-8")


def encode(string: str, method: callable) -> str:
    string = string.encode()
    digest = method(string)
    return digest.decode("utf-8")


def b64_decode(string: str) -> str:
    return decode(string, base64.b64decode)


def b32_decode(string: str) -> str:
    return decode(string, base64.b32decode, to_upper=True)


def b16_decode(string: str) -> str:
    return decode(string, base64.b16decode, to_upper=True)


def b64_encode(string: str) -> str:
    return encode(string, base64.b64encode)


def b32_encode(string: str) -> str:
    return encode(string, base64.b32encode)


def b16_encode(string: str) -> str:
    return encode(string, base64.b16encode)


name = "base"

actions = {
    "b64.decode": b64_decode,
    "b32.decode": b32_decode,
    "b16.decode": b16_decode,
    "b64.encode": b64_encode,
    "b32.encode": b32_encode,
    "b16.encode": b16_encode,
}
