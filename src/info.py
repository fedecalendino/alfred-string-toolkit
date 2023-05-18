def digits(string: str) -> int:
    string = string.lower()
    return len(list(filter(str.isdigit, string)))


def letters(string: str) -> int:
    string = string.lower()
    return len(list(filter(str.islower, string)))


def lenght(string: str) -> int:
    return len(string)


def words(string: str) -> int:
    return len(string.split(" "))


name = "info"

actions = {
    "digits": digits,
    "letters": letters,
    "lenght": lenght,
    "words": words,
}
