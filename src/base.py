import base64

from classes import Action


class DecodeAction(Action):
    def __init__(self, name: str, method: callable, to_upper: bool = False):
        super().__init__(name)

        self.method: callable = method
        self.to_upper: bool = to_upper

    def __call__(self, string: str) -> str:
        if self.to_upper:
            string = string.upper()

        digest = self.method(string)
        return digest.decode("utf-8")


class EncodeAction(Action):
    def __init__(self, name: str, method: callable):
        super().__init__(name)

        self.method: callable = method

    def __call__(self, string: str) -> str:
        string = string.encode()
        digest = self.method(string)
        return digest.decode("utf-8")


name = "base"

actions = [
    DecodeAction("b64.decode", base64.b64decode),
    DecodeAction("b32.decode", base64.b32decode, to_upper=True),
    DecodeAction("b16.decode", base64.b16decode, to_upper=True),
    EncodeAction("b64.encode", base64.b64encode),
    EncodeAction("b32.encode", base64.b32encode),
    EncodeAction("b16.encode", base64.b16encode),
]
