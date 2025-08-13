from classes import Action


class InfoAction(Action):
    def __init__(self, name: str, method: callable):
        super().__init__(name)
        self.method = method

    def __call__(self, string: str) -> int:
        return self.method(string)


name = "info"

actions = [
    InfoAction("string", lambda s: s),
    InfoAction("digits", lambda s: len(list(filter(str.isdigit, s.lower())))),
    InfoAction("letters", lambda s: len(list(filter(str.islower, s.lower())))),
    InfoAction("lenght", lambda s: len(s)),
    InfoAction("words", lambda s: len(s.split(" "))),
]
