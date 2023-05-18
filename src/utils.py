import ast
import base64
import json
import urllib.parse


def unquote(string: str) -> str:
    return urllib.parse.unquote(string)


def decodejwt(string: str) -> str:
    header, payload, signature = string.split(".")

    header = base64.b64decode(header + "===")
    payload = base64.b64decode(payload + "===")

    jwt = {
        "header": json.loads(header),
        "payload": json.loads(payload),
        "signature": signature,
    }

    return json.dumps(jwt), json.dumps(jwt, indent=2)


def dict_to_json(string: str) -> str:
    dictionary = ast.literal_eval(string)

    if not isinstance(dictionary, dict):
        return None

    return json.dumps(dictionary), json.dumps(dictionary, indent=2)


def indent_json(string: str) -> str:
    dictionary = json.loads(string)
    return json.dumps(dictionary), json.dumps(dictionary, indent=2)


def json_to_dict(string: str) -> str:
    dictionary = json.loads(string)
    return str(dictionary)


name = "utils"

actions = {
    "unquote": unquote,
    "decode-jwt": decodejwt,
    "dict-to-json": dict_to_json,
    "indent-json": indent_json,
    "json-to-dict": json_to_dict,
}
