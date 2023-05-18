import stringcase


def change_case(string: str, function: callable) -> str:
    result = function(string.lower())

    if result == string:
        return None

    return result


def lowercase(string: str) -> str:
    return string.lower()


def uppercase(string: str) -> str:
    return change_case(string, stringcase.uppercase)


def titlecase(string: str) -> str:
    return change_case(string, stringcase.titlecase)


def slugcase(string: str) -> str:
    return change_case(string, stringcase.spinalcase)


def snakecase(string: str) -> str:
    return change_case(string, stringcase.snakecase)


def constcase(string: str) -> str:
    return change_case(string, stringcase.constcase)


def pathcase(string: str) -> str:
    return change_case(string, stringcase.pathcase)


def nospaces(string: str) -> str:
    return change_case(string, lambda s: s.replace(" ", ""))


name = "case"

actions = {
    "lowercase": lowercase,
    "uppercase": uppercase,
    "titlecase": titlecase,
    "slugcase": slugcase,
    "snakecase": snakecase,
    "constcase": constcase,
    "pathcase": pathcase,
    "nospaces": nospaces,
}
