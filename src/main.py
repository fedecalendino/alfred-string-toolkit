import sys
import base64
import hashlib

import stringcase
from pyflow import Workflow

AFTER = "__after__"
BEFORE = "__before__"

FUNCTIONS = {
    "case": {
        BEFORE: str.lower,
        "lowercase": stringcase.lowercase,
        "uppercase": stringcase.uppercase,
        "titlecase": stringcase.titlecase,
        "slugcase": stringcase.spinalcase,
        "snakecase": stringcase.snakecase,
        "constcase": stringcase.constcase,
        "pathcase": stringcase.pathcase,
        "nospaces": lambda string: string.replace(" ", ""),
    },
    "base": {
        AFTER: lambda digest: digest.decode("utf-8"),
        "b64.decode": lambda text: base64.b64decode(text),
        "b32.decode": lambda text: base64.b32decode(text.upper()),
        "b16.decode": lambda text: base64.b16decode(text.upper()),
        "b64.encode": lambda text: base64.b64encode(text.encode()),
        "b32.encode": lambda text: base64.b32encode(text.encode()),
        "b16.encode": lambda text: base64.b16encode(text.encode()),
    },
    "hash": {
        BEFORE: lambda text: text.encode(),
        AFTER: lambda digest: digest.hexdigest(),
        "SHA3-512": lambda text: hashlib.sha3_512(text),
        "SHA3-384": lambda text: hashlib.sha3_384(text),
        "SHA3-256": lambda text: hashlib.sha3_256(text),
        "SHA3-224": lambda text: hashlib.sha3_224(text),
        "MD5": lambda text: hashlib.md5(text),
    },
    "info": {
        BEFORE: str.lower,
        "digits": lambda text: len(list(filter(str.isdigit, text))),
        "letters": lambda text: len(list(filter(str.islower, text))),
        "lenght": len,
        "words": lambda text: len(text.split(" ")),
    },
}


def main(workflow):
    command = workflow.args[0]
    string = " ".join(workflow.args[1:]).strip()

    before = FUNCTIONS[command].get(BEFORE, lambda _: _)
    after = FUNCTIONS[command].get(AFTER, lambda _: _)

    for name, converter in FUNCTIONS[command].items():
        if name in {BEFORE, AFTER}:
            continue

        try:
            value = after(converter(before(string)))
        except:
            continue

        if name != "lowercase" and value == string:
            continue

        workflow.new_item(
            title=value,
            subtitle=f" > {name}('{string}')",
            arg=value,
            valid=True,
        )


if __name__ == "__main__":
    wf = Workflow()
    wf.run(main)
    wf.send_feedback()
    sys.exit()
