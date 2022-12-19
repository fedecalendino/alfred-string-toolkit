import sys
from base64 import b64encode, b32encode, b16encode
from hashlib import sha512, sha384, sha256, sha224, sha1, md5

import stringcase
from pyflow import Workflow

FUNCTIONS = {
    "case": {
        "__before__": lambda text: text,
        "__after__": lambda text: text,
        "lower case": stringcase.lowercase,
        "upper case": stringcase.uppercase,
        "title case": stringcase.titlecase,
        "slug case": stringcase.spinalcase,
        "snake case": stringcase.snakecase,
        "const case": stringcase.constcase,
        "path case": stringcase.pathcase,
        "no spaces": lambda string: string.replace(" ", ""),
    },
    "base": {
        "__before__": lambda text: text.encode(),
        "__after__": lambda digest: digest.decode(),
        "base64": lambda text: b64encode(text),
        "base32": lambda text: b32encode(text),
        "base16": lambda text: b16encode(text),
    },
    "hash": {
        "__before__": lambda text: text.encode(),
        "__after__": lambda digest: digest.hexdigest(),
        "sha512": lambda text: sha512(text),
        "sha384": lambda text: sha384(text),
        "sha256": lambda text: sha256(text),
        "sha224": lambda text: sha224(text),
        "sha1": lambda text: sha1(text),
        "md5": lambda text: md5(text),
    },
    "info": {
        "__before__": lambda text: text,
        "__after__": lambda text: text,
        "lenght": len,
        "words": lambda text: len(text.split(" ")),
    },
}


def main(workflow):
    command = workflow.args[0]
    string = " ".join(workflow.args[1:]).lower().strip()

    before = FUNCTIONS[command]["__before__"]
    after = FUNCTIONS[command]["__after__"]

    for name, converter in FUNCTIONS[command].items():
        if name.startswith("__"):
            continue

        value = after(converter(before(string)))

        if name != "lower case" and value == string:
            continue

        workflow.new_item(
            title=value,
            subtitle=f" > {name.upper()}('{string}')",
            arg=value,
            valid=True,
        )


if __name__ == "__main__":
    wf = Workflow()
    wf.run(main)
    wf.send_feedback()
    sys.exit()
