import ast
import base64
import json
import urllib.parse

from classes import Action


class SortAction(Action):
    def __init__(self, reverse: bool = False):
        super().__init__("sort" if not reverse else "reverse")

        self.reverse: bool = reverse

    def __call__(self, string: str) -> str:
        lines = string.split("\n")
        lines.sort(reverse=self.reverse)

        return ", ".join(lines), "\n".join(lines)


class UnquoteAction(Action):
    def __init__(self):
        super().__init__("unquote")

    def __call__(self, string: str) -> str:
        return urllib.parse.unquote(string)


class DecodeJWTAction(Action):
    def __init__(self):
        super().__init__("decode-jwt")

    def __call__(self, string: str) -> str:
        header, payload, signature = string.split(".")

        header = base64.b64decode(header + "===")
        payload = base64.b64decode(payload + "===")

        jwt = {
            "header": json.loads(header),
            "payload": json.loads(payload),
            "signature": signature,
        }

        return json.dumps(jwt, indent=2)


class DictToJsonAction(Action):
    def __init__(self):
        super().__init__("dict-to-json")

    def __call__(self, string: str) -> str:
        dictionary = ast.literal_eval(string)

        if not isinstance(dictionary, dict):
            return None

        return json.dumps(dictionary, indent=2)


class IndentJsonAction(Action):
    def __init__(self):
        super().__init__("indent-json")

    def __call__(self, string: str) -> str:
        dictionary = json.loads(string)
        return json.dumps(dictionary, indent=2)


class JsonToDictAction(Action):
    def __init__(self):
        super().__init__("json-to-dict")

    def __call__(self, string: str) -> str:
        dictionary = json.loads(string)
        return str(dictionary)


name = "utils"

actions = [
    SortAction(),
    SortAction(reverse=True),
    UnquoteAction(),
    DecodeJWTAction(),
    DictToJsonAction(),
    JsonToDictAction(),
    IndentJsonAction(),
]
