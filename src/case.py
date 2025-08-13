import stringcase

from classes import Action


class CaseAction(Action):
    def __init__(self, name: str, function: callable):
        super().__init__(name)

        self.function = function

    def __call__(self, string: str) -> str:
        result = self.function(string.lower())

        if result == string:
            return None

        return result


name = "case"

actions = [
    CaseAction("lowercase", stringcase.lowercase),
    CaseAction("uppercase", stringcase.uppercase),
    CaseAction("titlecase", stringcase.titlecase),
    CaseAction("slugcase", stringcase.spinalcase),
    CaseAction("snakecase", stringcase.snakecase),
    CaseAction("constcase", stringcase.constcase),
    CaseAction("pathcase", stringcase.pathcase),
    CaseAction("nospaces", lambda s: s.replace(" ", "")),
]
